import json
from pathlib import Path

BASE_DIR = Path.home() / "Nobara_FF_UI"

DATA_FILE = BASE_DIR / "data.json"

data = {
    "character": "Nyxara",
    "world": "Omega",
    "zone": "Ul'dah",
    "job": "WAR",
    "gil": 777777
}

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("data.json updated")