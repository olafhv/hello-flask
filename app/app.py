#!/usr/bin/env python3
import ecs_logging
import logging
import os
from flask import Flask, request
from flask.logging import default_handler
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
handler = logging.StreamHandler()
handler.setFormatter(ecs_logging.StdlibFormatter())
logging.getLogger("werkzeug").removeHandler(default_handler)
logging.getLogger("werkzeug").addHandler(handler)
app.logger.removeHandler(default_handler)
app.logger.addHandler(handler)
metrics = PrometheusMetrics(app)

@app.route('/')
def index():
    app.logger.info("Hello from Python")
    return 'Hello from Python!'

app.run(host='0.0.0.0', port=8000)

