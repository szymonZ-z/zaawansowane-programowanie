from flask import Flask, request, jsonify
import uuid
import os
import requests
from api.rabbitmq import publish_task
from shared.storage import create_task, get_task

app = Flask(__name__)

IMAGES_DIR = "/app/shared/images"
os.makedirs(IMAGES_DIR, exist_ok=True)


@app.route("/analyze/local", methods=["GET"])
def analyze_local():
    path = request.args.get("path")
    if not path or not os.path.exists(path):
        return jsonify({"error": "Plik nie istnieje"}), 404

    task_id = str(uuid.uuid4())
    create_task(task_id)

    publish_task({
        "task_id": task_id,
        "image_path": path
    })

    return jsonify({"task_id": task_id})


@app.route("/analyze/url", methods=["GET"])
def analyze_url():
    image_url = request.args.get("image_url")
    if not image_url:
        return jsonify({"error": "Brak URL"}), 400

    task_id = str(uuid.uuid4())
    create_task(task_id)

    local_path = f"{IMAGES_DIR}/{task_id}.jpg"
    response = requests.get(image_url)

    with open(local_path, "wb") as f:
        f.write(response.content)

    publish_task({
        "task_id": task_id,
        "image_path": local_path
    })

    return jsonify({"task_id": task_id})


@app.route("/analyze/upload", methods=["POST"])
def analyze_upload():
    if "file" not in request.files:
        return jsonify({"error": "Brak pliku"}), 400

    file = request.files["file"]
    task_id = str(uuid.uuid4())
    create_task(task_id)

    file_path = f"{IMAGES_DIR}/{task_id}_{file.filename}"
    file.save(file_path)

    publish_task({
        "task_id": task_id,
        "image_path": file_path
    })

    return jsonify({"task_id": task_id})


@app.route("/tasks/<task_id>", methods=["GET"])
def task_status(task_id):
    task = get_task(task_id)
    if not task:
        return jsonify({"error": "Nie znaleziono zadania"}), 404
    return jsonify(task)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
