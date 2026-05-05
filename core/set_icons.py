import os
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

# Mapowanie skrótów z gry na nazwy plików (zgodnie z Twoim folderem icons)
JOB_MAP = {
    # Tanki
    "WAR": "Warrior", "PLD": "Paladin", "DRK": "DarkKnight", "GNB": "Gunbreaker",
    # Healerzy
    "WHM": "WhiteMage", "SCH": "Scholar", "AST": "Astrologian", "SGE": "Sage",
    # DPS (Melee)
    "MNK": "Monk", "DRG": "Dragoon", "NIN": "Ninja", "SAM": "Samurai", "RPR": "Reaper", "VPR": "Viper",
    # DPS (Range/Caster)
    "BRD": "Bard", "MCH": "Machinist", "DNC": "Dancer", "BLM": "BlackMage", "SMN": "Summoner", "RDM": "RedMage",
    "PCT": "Pictomancer",
    # Inne/Crafterzy (używane w Alliance C)
    "ALC": "Alchemist", "MIN": "Miner", "BTN": "Botanist", "FSH": "Fisher", "NONE": "EmptySlot"
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS_PATH = os.path.join(BASE_DIR, "assets", "icons")


def get_job_icon(job_code, size=20):
    """Pobiera ikonę na podstawie kodu (np. 'VPR') lub nazwy specjalnej (np. 'gil')"""
    job_code = str(job_code).upper()

    # Jeśli to 'NONE', szukamy specjalnego pliku lub zwracamy pusty pixmap
    if job_code == "NONE":
        return QPixmap()

    # Sprawdź mapowanie, jeśli nie ma - spróbuj użyć kodu jako nazwy (np. dla 'gil')
    file_name = JOB_MAP.get(job_code, job_code.capitalize())
    file_path = os.path.join(ICONS_PATH, f"{file_name}.png")

    if not os.path.exists(file_path):
        # Fallback na Gil.png jeśli nic nie pasuje
        file_path = os.path.join(ICONS_PATH, "Gil.png")

    pixmap = QPixmap(file_path)
    if pixmap.isNull():
        return QPixmap()

    return pixmap.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)