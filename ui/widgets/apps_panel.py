from ui.widgets.base_panel import BasePanel
from modules.alliance.alliance_c_apps.running_apps import get_running_apps


APP_ICONS = {
    "discord": "discord_app",
    "vesktop": "discord_app",
    "firefox": "firefox",
    "chrome": "browser",
    "steam": "steam",
    "xivlauncher": "ffxiv",
    "obs": "obs",
    "spotify": "music",
    "thunderbird": "message",
    "pycharm": "apps",
    "kitty": "terminal",
    "dolphin": "files",
    "waybar": "system"
}


def get_app_icon(app_name: str):
    lower = app_name.lower()

    for key, icon in APP_ICONS.items():
        if key in lower:
            return icon

    return "apps"


class AppsPanel(BasePanel):
    def __init__(self):
        super().__init__("ALLIANCE C / APPS", "apps")

        self.rows = []

        for _ in range(8):
            self.rows.append(self.add_line("-", "apps"))

    def refresh(self):
        apps = get_running_apps()

        for line, app in zip(self.rows, apps[:8]):
            icon = get_app_icon(app)
            self.set_line(line, app, icon)