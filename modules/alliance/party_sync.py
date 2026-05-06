import json
from pathlib import Path

BASE_DIR = Path.home() / "Nobara_FF_UI"

FILE = BASE_DIR / "modules" / "alliance" / "alliance.json"


def load_alliance():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_alliance(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def add_member(group, member):
    data = load_alliance()

    if member not in data[group]["members"]:
        data[group]["members"].append(member)

    save_alliance(data)


def remove_member(group, member):
    data = load_alliance()

    if member in data[group]["members"]:
        data[group]["members"].remove(member)

    save_alliance(data)