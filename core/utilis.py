import time
import math


def get_eorzea_time():
    """
    Przelicza czas systemowy (UTC) na czas Eorzea.
    Eorzea Time płynie dokładnie 20.571428571428573 razy szybciej niż czas ziemski.
    """
    # Stała przelicznika czasu Eorzea
    EORZEA_CONSTANT = 20.571428571428573

    # Pobieramy aktualny czas Unix
    now = time.time()

    # Obliczamy całkowitą liczbę sekund Eorzea, które upłynęły
    eorzea_seconds = now * EORZEA_CONSTANT

    # Przeliczamy na minuty, godziny
    v_min = int((eorzea_seconds / 60) % 60)
    v_hr = int((eorzea_seconds / 3600) % 24)

    return f"{v_hr:02d}:{v_min:02d}"


def get_hp_color(percentage):
    """
    Zwraca kolor Hex w zależności od procentu (użyteczne dla paska HP/Hardware).
    Mapowanie na barwy FF XIV.
    """
    if percentage > 75:
        return "#3fb361"  # Zielony (Zdrowy)
    elif percentage > 25:
        return "#f1c40f"  # Żółty (Warning)
    else:
        return "#ff4b4b"  # Czerwony (Critical)


def format_to_waybar(text, alt="", class_name="", percentage=-1):
    """
    Formatuj dane do standardu JSON, który Waybar rozumie jako 'return-type': 'json'
    """
    res = {
        "text": str(text),
        "alt": str(alt),
        "class": str(class_name)
    }
    if percentage >= 0:
        res["percentage"] = int(percentage)

    return res


def get_job_icon(job_name):
    """
    Zwraca odpowiedni symbol fontu dla profesji.
    Wymaga zainstalowanego fontu z ikonami FF XIV lub Nerd Fonts.
    """
    icons = {
        "tank": "",
        "healer": "",
        "dps": "",
        "cpu": "",
        "gpu": "󰢮",
        "ram": ""
    }
    return icons.get(job_name.lower(), "")


def calculate_progress_bar(current, total, width=10):
    """
    Tworzy tekstowy pasek postępu (przydatne do logów terminala lub prostych widgetów).
    """
    percent = (current / total)
    filled = int(width * percent)
    bar = "▰" * filled + "▱" * (width - filled)
    return bar