import os
from datetime import datetime
import json



# -----------------------------
# File paths (simple persistence)
# -----------------------------
BASE_DIR = "storage"
NOTES_FILE = os.path.join(BASE_DIR, "notes.json")
os.makedirs(BASE_DIR, exist_ok=True)

def load_json(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        return json.load(f)

def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

def new_notes(title: str, content: str) -> dict:
    """Add a new note"""
    notes = load_json(NOTES_FILE)

    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "created_at": datetime.now().isoformat()
    }

    notes.append(note)
    save_json(NOTES_FILE, notes)

    return {"status": "success", "message": "Note added", "note": note}

def fetch_notes() -> dict:
    """Fetch all notes"""
    return {"notes": load_json(NOTES_FILE)}