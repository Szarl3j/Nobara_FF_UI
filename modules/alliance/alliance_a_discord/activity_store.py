import time
from core.paths import DISCORD_ACTIVITY_FILE
from core.state import load_json, save_json


def get_activity():
    return load_json(DISCORD_ACTIVITY_FILE, {"activity": []})


def register_activity(name: str, message: str = "", source: str = "notification"):
    data = get_activity()
    activity = data.get("activity", [])

    existing = None

    for item in activity:
        if item.get("name") == name:
            existing = item
            break

    if existing:
        activity.remove(existing)
    else:
        existing = {}

    existing["name"] = name
    existing["message"] = message
    existing["source"] = source
    existing["timestamp"] = int(time.time())
    existing["glow"] = True

    activity.insert(0, existing)

    data["activity"] = activity[:50]
    save_json(DISCORD_ACTIVITY_FILE, data)


def clear_glow(name: str | None = None):
    data = get_activity()

    for item in data.get("activity", []):
        if name is None or item.get("name") == name:
            item["glow"] = False

    save_json(DISCORD_ACTIVITY_FILE, data)