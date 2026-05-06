import json
from pathlib import Path

BASE_DIR = Path.home() / "Nobara_FF_UI"

DATA_FILE = BASE_DIR / "data.json"

try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    character = data.get("character", "Unknown")
    world = data.get("world", "Unknown")
    zone = data.get("zone", "Unknown")

    print(f"{character} | {world} | {zone}")

except Exception:
    print("FFXIV Offline")