import json
import os

TASKS_FILE = "/app/shared/tasks.json"


def _load_tasks():
    if not os.path.exists(TASKS_FILE):
        return {}

    try:
        with open(TASKS_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except json.JSONDecodeError:
        return {}


def _save_tasks(tasks: dict):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)


def create_task(task_id: str):
    tasks = _load_tasks()
    tasks[task_id] = {
        "status": "queued",
        "people_count": None,
        "result_image": None
    }
    _save_tasks(tasks)


def update_task(task_id: str, status: str, count=None, image=None):
    tasks = _load_tasks()

    if task_id not in tasks:
        tasks[task_id] = {
            "status": "queued",
            "people_count": None,
            "result_image": None
        }

    tasks[task_id]["status"] = status
    if count is not None:
        tasks[task_id]["people_count"] = count
    if image is not None:
        tasks[task_id]["result_image"] = image

    _save_tasks(tasks)


def get_task(task_id: str):
    tasks = _load_tasks()
    return tasks.get(task_id)
