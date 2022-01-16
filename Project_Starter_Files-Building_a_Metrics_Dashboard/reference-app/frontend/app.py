import logging
from flask_cors import CORS
from flask import Flask, render_template, request
from jaeger_client import Config
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics


def init_tracer(service):
    logging.getLogger("").handlers = []
    logging.basicConfig(format="%(message)s", level=logging.DEBUG)
    config = Config(
        config={
            "sampler": {"type": "const", "param": 1},
            "logging": True,
            "reporter_batch_size": 1,
        },
        service_name=service,
        validate=True,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()

tracer = init_tracer("frontend-service")


app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

CORS(app)

metrics = GunicornInternalPrometheusMetrics(app, group_by='endpoint')
metrics.info('frontend', 'Frontend Metrics', version='1.0.3')

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
def frontend_homepage():
    with tracer.start_span('frontend-homepage') as span:
        span.set_tag('message', 'frontend homepage')
    return render_template("main.html")

if __name__ == "__main__":
    app.run()
