import json
from pathlib import Path

BASE_DIR = Path.home() / "Nobara_FF_UI"

FILE = BASE_DIR / "modules" / "discord" / "discord_groups.json"

try:
    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    groups = len(data.keys())

    print(f"Discord Groups: {groups}")

except Exception:
    print("Discord Error")