import platform
import shutil
import subprocess
from pathlib import Path

from core.paths import SOUNDS_DIR


RINGTONES_DIR = SOUNDS_DIR / "ringtones"

IS_WINDOWS = platform.system() == "Windows"


def get_player():
    """
    Szuka odtwarzacza.
    """

    players = [
        "mpv",
        "vlc"
    ]

    for player in players:
        path = shutil.which(player)

        if path:
            return path

    return None


def play_file(path: Path):
    if not path.exists():
        return False

    player = get_player()

    if not player:
        print("No audio player found (mpv/vlc)")
        return False

    try:
        if "mpv" in player.lower():
            subprocess.Popen([
                player,
                "--no-video",
                "--really-quiet",
                str(path)
            ])

        else:
            subprocess.Popen([
                player,
                str(path)
            ])

        return True

    except Exception as e:
        print(f"Sound error: {e}")
        return False


def play(sound_name: str):
    candidates = [
        RINGTONES_DIR / f"{sound_name}.mp3",
        SOUNDS_DIR / f"{sound_name}.mp3"
    ]

    for file in candidates:
        if play_file(file):
            return True

    return False


def play_from_ringtones(sound_name: str):
    return play_file(RINGTONES_DIR / f"{sound_name}.mp3")


def play_from_sounds(sound_name: str):
    return play_file(SOUNDS_DIR / f"{sound_name}.mp3")