#!/usr/bin/env python3
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def index():
    return 'Hello from Python!'


print("Pod strated %s" % os.environ)
app.run(host='0.0.0.0', port=8000)

