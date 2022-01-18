import logging
from flask_cors import CORS
from flask import Flask, render_template, request, jsonify, Response
from flask_opentracing import FlaskTracing
from jaeger_client import Config
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
import pymongo
from flask_pymongo import PyMongo
import time
import random
import threading


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
        #metrics_factory=PrometheusMetricsFactory(service_name_label=service),
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()
    
tracer = init_tracer("backend-service")


app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
#flask_tracer = FlaskTracing(tracer)
#flask_tracer = FlaskTracing(tracer, True, app)

CORS(app)

# metrics = PrometheusMetrics(app)
metrics = GunicornInternalPrometheusMetrics(app, group_by='endpoint')
# static information as metric
#metrics.info("app_info", "Application info", version="1.0.3")
metrics.info('backend_info', 'Backend Metrics', version='1.0.3')

metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths', labels={'path': lambda: request.path}
    )
)

endpoint_counter = metrics.counter(
    'by_endpoint_counter', 'Request count by endpoints',
    labels={'endpoint': lambda: request.endpoint}
)

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config["MONGO_URI"] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"
mongo = PyMongo(app)

@app.route("/")
@endpoint_counter
#@flask_tracer.trace()
def backend_homepage():
    with tracer.start_span('hello-span') as span:
        span.set_tag('Start', "Hello World")
        time.sleep(random.random() * 0.4)
        answer = "Hello World"
        span.set_tag('End', "Hello World")
    return jsonify(response=answer)


@app.route("/api")
@endpoint_counter
def backend_api():
    global current_mode
    current_mode = 'normal'
    modes = ('normal', '400', '500')

    with tracer.start_span('api-span') as span:
        span.set_tag('Start', "Hbackend_api")
        time.sleep(random.random() * 0.4)
        draw = random.choice(modes)
        draw_again = random.choice(modes)
        if draw == draw_again:
            current_mode = draw
        answer = "something"
        span.set_tag('End', "Hbackend_api")
        if current_mode == '500':
            return ':(', 500
        elif current_mode == '400':
            return ':|', 400
        else:
            jsonify(response=answer)

@app.route("/star", methods=["POST"])
@endpoint_counter
def backend_star():
    with tracer.start_span('add star') as span:
        span.set_tag('Start', "backend_star")
        #req = request.get_json()
        star = mongo.db.stars
        name = request.get_json['name']
        distance = request.get_json['distance']
        star_id = star.insert({'name': name, 'distance': distance})
        new_star = star.find_one({'_id': star_id })
        output = {'name' : new_star['name'], 'distance' : new_star['distance']}
        span.set_tag('End', "backend_star")
        return jsonify({'result' : output})     

if __name__ == "__main__":
    app.run()
