import os
from datetime import datetime
import json


BASE_DIR = "storage"
REMINDERS_FILE = os.path.join(BASE_DIR, "reminders.json")


def load_json(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        return json.load(f)

def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

def create_reminder(task: str, time: str) -> dict:
    """Add a reminder"""
    reminders = load_json(REMINDERS_FILE)

    reminder = {
        "id": len(reminders) + 1,
        "task": task,
        "time": time,
        "created_at": datetime.now().isoformat()
    }

    reminders.append(reminder)
    save_json(REMINDERS_FILE, reminders)

    return {"status": "success", "message": "Reminder added", "reminder": reminder}



def fetch_reminders() -> dict:
    """Fetch all reminders"""
    return {"reminders": load_json(REMINDERS_FILE)}