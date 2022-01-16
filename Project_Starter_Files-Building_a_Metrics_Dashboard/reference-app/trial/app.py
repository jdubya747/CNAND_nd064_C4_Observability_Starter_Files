import logging
from os import spawnl
import re
import requests
from flask_cors import CORS
from flask import Flask, request, Response
from jaeger_client import Config
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

def custom_rule(req):  # the Flask request object
    """ The name of the function becomes the label name. """
    return '%s::%s' % (req.method, req.path)
def init_tracer(service):
    logging.getLogger("").handlers = []
    logging.basicConfig(format="%(message)s", level=logging.DEBUG)
    #logger = logging.getLogger(__name__)
    config = Config(
        config={
            "sampler": {"type": "const", "param": 1},
            "logging": True,
            "reporter_batch_size": 1,
        },
        service_name=service,
        validate=True,
    )

    return config.initialize_tracer()

tracer = init_tracer("trial-service")

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

CORS(app)
#'endpoint'
metrics = GunicornInternalPrometheusMetrics(app, group_by='endpoint')
metrics.info('trial', 'trial Metrics', version='1.0.3')

#custom_rule
metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths', labels={'path': lambda: request.path}
    )
)

endpoint_counter = metrics.counter(
    'by_endpoint_counter', 'Request count by endpoints',
    labels={'endpoint': lambda: request.endpoint}
)


@app.route("/")
@endpoint_counter
def trial_homepage():
    counter = 0
    response = Response(status=200)
    url_string = 'https://api.openbrewerydb.org/breweries'
    with tracer.start_span('get-beer-opportunities') as span:
        span.set_tag("URL", url_string)
        biers = []
        res = requests.get(url_string)
        span.set_tag('request-type', 'Success')
        span.log_kv({"event": "get breweries count", "count": len(res.json())})
  
        for brewpub in res.json():
            with tracer.start_span(brewpub['name'], child_of=span) as site_span:
                #logger.info(f"Getting website for {brewpub['name']}")
                try:
                    counter = counter + 1
                    if counter > 3:
                        break
                    site_span.set_tag("URL", url_string)
                    full_mug = requests.get(brewpub['website_url'])
                    biers.append(full_mug)
                    site_span.set_tag('request-type', 'Success')
                except Exception as ex:
                    site_span.set_tag('request-type', 'Failure')
    return response


def remove_tags(text):
    tag = re.compile(r"<[^>]+>")
    return tag.sub("", text)


@app.route("/trace")
@endpoint_counter
def trial_trace():
    response = Response(status=200)
    with tracer.start_span("get-python-jobs") as span:
        url = "https://jobs.github.com/positions.json?description=python"
        res = requests.get(url)
        span.log_kv({"event": "get jobs count", "count": len(res.json())})
        span.set_tag("URL", url)
        jobs_info = []
        for result in res.json():
            jobs = {}
            with tracer.start_span(result['company'], child_of=span) as site_span:
                try:
                    home = requests.get(result['company_url'])
                    site_span.set_tag('request-type', 'Success')
                    jobs["description"] = remove_tags(result["description"])
                    jobs["company"] = result["company"]
                    jobs["company_url"] = result["company_url"]
                    jobs["created_at"] = result["created_at"]
                    jobs["how_to_apply"] = result["how_to_apply"]
                    jobs["location"] = result["location"]
                    jobs["title"] = result["title"]
                    jobs["type"] = result["type"]
                    jobs["url"] = result["url"]
                    jobs_info.append(jobs)
                except Exception as ex:
                    site_span.set_tag('request-type', 'Failure')
    return response

if __name__ == "__main__":
    app.run(debug=True,)
