from flask import Flask, Response
from prometheus_client import Counter, Summary, generate_latest, CONTENT_TYPE_LATEST
import random

app = Flask(__name__)

# Prometheus counters
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', 
                        ['status', 'endpoint', 'method'])
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route("/")
@REQUEST_TIME.time()
def index():
    # Randomly simulate 500 errors ~20% of the time
    endpoint = "/"
    method = "GET"
    if random.random() < 0.2:
        REQUEST_COUNT.labels(status="500", 
                             endpoint=endpoint, 
                             method=method).inc()
        return "Internal Server Error", 500
    else:
        REQUEST_COUNT.labels(status="200", 
                             endpoint=endpoint, 
                             method=method).inc()
        return "Hello, world!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
