from pathlib import Path

BASE_DIR = Path.home() / "Nobara_FF_UI"

WALLPAPER_DIR = BASE_DIR / "assets" / "wallpapers"

files = list(WALLPAPER_DIR.glob("*.mp4"))

for file in files:
    print(file.name)