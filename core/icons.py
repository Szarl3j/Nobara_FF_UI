from pathlib import Path

from PySide6.QtGui import QIcon, QPixmap

from core.paths import ICONS_DIR


ICON_ALIASES = {
    # Discord / Alliance A
    "discord": "Bard.png",
    "message": "Scholar.png",
    "notification": "Astrologian.png",

    # System / Alliance B
    "cpu": "Blacksmith.png",
    "gpu": "Machinist.png",
    "ram": "Scholar.png",
    "vram": "Sage.png",
    "disk": "Miner.png",
    "network": "Ninja.png",
    "temperature": "RedMage.png",
    "system": "Gunbreaker.png",

    # Apps / Alliance C
    "apps": "Summoner.png",
    "steam": "Warrior.png",
    "browser": "Pictomancer.png",
    "firefox": "Pictomancer.png",
    "discord_app": "Bard.png",
    "terminal": "BlackMage.png",
    "files": "Carpenter.png",
    "obs": "Machinist.png",
    "music": "Dancer.png",

    # Quest Log / TODO
    "todo": "Paladin.png",
    "school": "WhiteMage.png",
    "work": "DarkKnight.png",
    "ffxiv": "TankRole.png",
    "done": "Done.png",

    # Currency / misc
    "gil": "gil.png",
    "default": "Adventurer.png"
}


def get_icon_path(name: str) -> Path | None:
    if not name:
        return None

    icon_file = ICON_ALIASES.get(name.lower(), name)

    path = ICONS_DIR / icon_file

    if path.exists():
        return path

    return None


def get_qicon(name: str) -> QIcon:
    path = get_icon_path(name)

    if not path:
        return QIcon()

    return QIcon(str(path))


def get_pixmap(name: str, size: int = 24) -> QPixmap:
    path = get_icon_path(name)

    if not path:
        return QPixmap()

    pixmap = QPixmap(str(path))

    return pixmap.scaled(size, size)