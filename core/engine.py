import json
import random
import time
from pathlib import Path

BASE_DIR = Path.home() / "Nobara_FF_UI"

DATA_FILE = BASE_DIR / "data.json"

jobs = ["WAR", "DRK", "WHM", "SGE", "SAM", "VPR"]

while True:
    data = {
        "character": "Nyxara",
        "world": "Omega",
        "zone": "Ul'dah",
        "job": random.choice(jobs),
        "gil": random.randint(100000, 999999)
    }

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    time.sleep(5)