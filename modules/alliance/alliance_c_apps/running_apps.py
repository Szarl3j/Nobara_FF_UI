import psutil
from core.paths import APPS_STATUS_FILE
from core.state import save_json


IMPORTANT_APPS = [
    "discord",
    "vesktop",
    "firefox",
    "chrome",
    "steam",
    "xivlauncher",
    "XIVLauncher.Core",
    "obs",
    "spotify",
    "thunderbird",
    "pycharm",
    "kitty",
    "dolphin",
    "waybar"
    "Brave"
    "Word"
    "PowerPoint"
    "Thunderbird"
    "IntelliJ IDEA Ultimate"
    "IntelliJ IDEA Community Edition"
    "JetBrains Toolbox"
    "WebStorm"

]


def get_running_apps():
    found = []

    for proc in psutil.process_iter(["name"]):
        try:
            name = proc.info.get("name")

            if not name:
                continue

            lower = name.lower()

            for app in IMPORTANT_APPS:
                if app.lower() in lower and app not in found:
                    found.append(app)

            if len(found) >= 8:
                break

        except Exception:
            pass

    while len(found) < 8:
        found.append("-")

    save_json(APPS_STATUS_FILE, {"apps": found[:8]})

    return found[:8]