from flask import Flask, request, jsonify
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from metrics import TASK_DURATION
from config import load_config
import logging

app = Flask(__name__)
config = load_config()

logging.basicConfig(level=config["LOG_LEVEL"])


@app.route('/api/tasks', methods=['POST'])
def receive_task():
    data = request.get_json()
    required_keys = {"tool", "task", "status", "duration"}

    if not data or not required_keys.issubset(data.keys()):
        return jsonify({"error": "Invalid task data"}), 400

    status = data["status"]
    if status not in {"completed", "failed", "succeeded"}:
        return jsonify({"error": "Invalid status value"}), 400

    try:
        duration = float(data["duration"])
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid duration"}), 400

    TASK_DURATION.labels(tool=data["tool"], task=data["task"]).set(duration)
    return jsonify({"message": "Task received"}), 200


@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


if __name__ == '__main__':
    app.run(host=config["HOST"], port=config["PORT"])
