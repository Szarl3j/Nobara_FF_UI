from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

# ASSETS

ASSETS_DIR = BASE_DIR / "assets"

ICONS_DIR = ASSETS_DIR / "icons"
SOUNDS_DIR = ASSETS_DIR / "sounds"
VIDEOS_DIR = ASSETS_DIR / "videos"
WALLPAPERS_DIR = ASSETS_DIR / "wallpapers"

# CONFIG

CONFIG_DIR = BASE_DIR / "config"

APP_CONFIG_FILE = CONFIG_DIR / "app.json"
PATHS_CONFIG_FILE = CONFIG_DIR / "paths.json"
QUEST_LOG_CONFIG_FILE = CONFIG_DIR / "quest_log.json"

HOTBAR_CONFIG_FILE = CONFIG_DIR / "hotbar.json"

THRESHOLDS_CONFIG_FILE = CONFIG_DIR / "thresholds.json"

DISCORD_LISTENER_CONFIG_FILE = CONFIG_DIR / "discord_listener.json"

HUD_LAYOUT_CONFIG_FILE = CONFIG_DIR / "hud_layout.json"

# STATE

STATE_DIR = BASE_DIR / "state"

DISCORD_ACTIVITY_FILE = STATE_DIR / "discord_activity.json"

SYSTEM_STATUS_FILE = STATE_DIR / "system_status.json"

APPS_STATUS_FILE = STATE_DIR / "apps_status.json"

UI_STATE_FILE = STATE_DIR / "ui_state.json"

# OTHER

LOGS_DIR = BASE_DIR / "logs"

MODULES_DIR = BASE_DIR / "modules"

UI_DIR = BASE_DIR / "ui"

WAYBAR_DIR = BASE_DIR / "waybar"

DATA_FILE = BASE_DIR / "data.json"


def ensure_directories():
    directories = [
        CONFIG_DIR,
        STATE_DIR,
        LOGS_DIR
    ]

    for directory in directories:
        directory.mkdir(
            parents=True,
            exist_ok=True
        )