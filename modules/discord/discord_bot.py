import os
import json
from pathlib import Path

import discord

BASE_DIR = Path.home() / "Nobara_FF_UI"
CONFIG_FILE = BASE_DIR / "modules" / "discord" / "discord_config.json"
LOG_FILE = BASE_DIR / "logs" / "discord.log"

with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    config = json.load(f)

token = os.getenv(config.get("token_env", "NOBARA_FF_DISCORD_TOKEN"))

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)


def write_log(text):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")


@client.event
async def on_ready():
    write_log(f"READY: {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    watch_channels = config.get("watch_channels", [])

    if watch_channels and str(message.channel.id) not in watch_channels:
        return

    text = f"[{message.guild}] #{message.channel} {message.author}: {message.content}"
    write_log(text)


if __name__ == "__main__":
    if not token:
        print("Brak tokena w zmiennej środowiskowej.")
        print("Ustaw: export NOBARA_FF_DISCORD_TOKEN='TOKEN'")
    else:
        client.run(token)