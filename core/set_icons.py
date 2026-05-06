from pathlib import Path

BASE_DIR = Path.home() / "Nobara_FF_UI"

ICON_DIR = BASE_DIR / "assets" / "icons"

ICONS = {
    "WAR": "war.png",
    "DRK": "drk.png",
    "WHM": "whm.png",
    "SGE": "sge.png",
    "SAM": "sam.png",
    "VPR": "vpr.png"
}


def get_job_icon(job):
    file = ICONS.get(job)

    if not file:
        return None

    return ICON_DIR / file


def get_icon(name):
    return get_job_icon(name)