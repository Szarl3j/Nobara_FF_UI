import json
from pathlib import Path

BASE_DIR = Path.home() / "Nobara_FF_UI"

DATA_FILE = BASE_DIR / "data.json"

try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(data.get("job", "WAR"))

except Exception:
    print("JOB")