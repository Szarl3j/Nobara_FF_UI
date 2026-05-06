import subprocess
from pathlib import Path

BASE_DIR = Path.home() / "Nobara_FF_UI"
LOG_FILE = BASE_DIR / "logs" / "discord.log"


def notify(title, message):
    subprocess.Popen(["notify-send", title, message])
    subprocess.Popen(["play-sound", "notification"])


if __name__ == "__main__":
    notify("Discord", "Nowa aktywność Discord")