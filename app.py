
from flask import Flask, jsonify, request, Response
import os
import time

from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Application state
healthy = True

# Monitoring metrics
start_time = time.time()

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status"]
)

APP_HEALTH = Gauge(
    "app_health",
    "Application health status (1=healthy, 0=unhealthy)"
)

# Sample tasks
tasks = [
    {"id": 1, "title": "Learn Linux commands", "completed": False},
    {"id": 2, "title": "Build Podman container", "completed": False},
    {"id": 3, "title": "Deploy to OpenShift", "completed": False}
]


@app.get("/health")
def health():
    if not healthy:
        REQUEST_COUNT.labels(
            method="GET",
            endpoint="/health",
            status="500"
        ).inc()

        APP_HEALTH.set(0)

        return jsonify(status="unhealthy"), 500

    REQUEST_COUNT.labels(
        method="GET",
        endpoint="/health",
        status="200"
    ).inc()

    APP_HEALTH.set(1)

    return jsonify(status="healthy"), 200


@app.get("/status")
def status():
    REQUEST_COUNT.labels(
        method="GET",
        endpoint="/status",
        status="200"
    ).inc()

    return jsonify(
        app_name=os.getenv("APP_NAME", "Self-Healing API"),
        environment=os.getenv("ENVIRONMENT", "development"),
        healthy=healthy,
        hostname=os.uname().nodename
    )


@app.get("/tasks")
def get_tasks():
    REQUEST_COUNT.labels(
        method="GET",
        endpoint="/tasks",
        status="200"
    ).inc()

    return jsonify(tasks)


@app.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")

    if not title:
        REQUEST_COUNT.labels(
            method="POST",
            endpoint="/tasks",
            status="400"
        ).inc()

        return jsonify(error="title is required"), 400

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)

    REQUEST_COUNT.labels(
        method="POST",
        endpoint="/tasks",
        status="201"
    ).inc()

    return jsonify(task), 201


@app.get("/fail")
def fail():
    global healthy

    healthy = False
    APP_HEALTH.set(0)

    REQUEST_COUNT.labels(
        method="GET",
        endpoint="/fail",
        status="200"
    ).inc()

    return jsonify(message="Application marked unhealthy"), 200


@app.get("/metrics")
def metrics():
    APP_HEALTH.set(1 if healthy else 0)

    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


@app.get("/uptime")
def uptime():
    REQUEST_COUNT.labels(
        method="GET",
        endpoint="/uptime",
        status="200"
    ).inc()

    return jsonify(
        uptime_seconds=round(time.time() - start_time, 2)
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
