import re
import subprocess

from core.paths import DISCORD_LISTENER_CONFIG_FILE
from core.state import load_json
from core.sound import play
from modules.alliance.alliance_a_discord.activity_store import register_activity

DEFAULT_CONFIG = {
    "enabled": True,
    "keywords": ["discord", "vesktop", "webcord", "discord.com"],
    "ignored_titles": ["Discord", "Vesktop", "WebCord", "Google Chrome", "Firefox"],
    "play_sound_on_message": True,
    "message_sound": "ffxiv-message-2"
}


def load_config():
    return load_json(DISCORD_LISTENER_CONFIG_FILE, DEFAULT_CONFIG)


def looks_like_discord(text: str, keywords):
    lower = text.lower()
    return any(keyword.lower() in lower for keyword in keywords)


def extract_strings(text: str):
    return re.findall(r'string\s+"([^"]+)"', text)


def extract_sender(text: str, ignored_titles):
    strings = extract_strings(text)

    for value in strings:
        value = value.strip()

        if not value:
            continue

        if value in ignored_titles:
            continue

        if len(value) > 80:
            continue

        return value

    return None


def listen():
    config = load_config()

    if not config.get("enabled", True):
        return

    process = subprocess.Popen(
        [
            "dbus-monitor",
            "interface='org.freedesktop.Notifications',member='Notify'"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )

    buffer = []

    for line in process.stdout:
        buffer.append(line.strip())

        if len(buffer) >= 35:
            text = "\n".join(buffer)

            if looks_like_discord(text, config.get("keywords", [])):
                sender = extract_sender(
                    text,
                    config.get("ignored_titles", [])
                )

                if sender:
                    register_activity(
                        sender,
                        "Discord notification",
                        "notification"
                    )

                    if config.get("play_sound_on_message", True):
                        play(config.get("message_sound", "ffxiv-message-2"))

            buffer = []


if __name__ == "__main__":
    listen()