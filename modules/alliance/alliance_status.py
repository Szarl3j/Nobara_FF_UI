import json
from pathlib import Path

BASE_DIR = Path.home() / "Nobara_FF_UI"

FILE = BASE_DIR / "modules" / "alliance" / "alliance.json"

try:
    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    a = len(data["alliance_a"]["members"])
    b = len(data["alliance_b"]["members"])
    c = len(data["alliance_c"]["members"])

    print(f"A:{a}  B:{b}  C:{c}")

except Exception:
    print("Alliance Error")