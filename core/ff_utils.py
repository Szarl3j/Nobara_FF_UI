import json
from pathlib import Path

BASE_DIR = Path.home() / "Nobara_FF_UI"

DATA_FILE = BASE_DIR / "data.json"


def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:
        return {}