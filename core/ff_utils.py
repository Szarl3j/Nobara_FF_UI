import time
import math
import datetime

def get_eorzea_time():
    """
    Przelicza czas systemowy (Unix) na czas Eorzea.
    Eorzea Time płynie dokładnie 20.571428571428573 razy szybciej niż czas ziemski.
    """
    EORZEA_CONSTANT = 20.571428571428573
    now = time.time()
    eorzea_seconds = now * EORZEA_CONSTANT

    v_min = int((eorzea_seconds / 60) % 60)
    v_hr = int((eorzea_seconds / 3600) % 24)

    return f"{v_hr:02d}:{v_min:02d}"

def format_gil(value):
    """
    Formatuje liczbę na format waluty Gil (np. 1 234 567).
    Używane do wyświetlania stanu posiadania lub wolnego miejsca jako Gil.
    """
    try:
        return "{:,.0f}".format(float(value)).replace(",", " ")
    except (ValueError, TypeError):
        return "0"

def get_hp_color(percentage):
    """
    Zwraca kolor Hex w zależności od procentu (barwy FF XIV).
    """
    if percentage > 75:
        return "#3fb361"  # Zielony
    elif percentage > 25:
        return "#f1c40f"  # Żółty
    else:
        return "#ff4b4b"  # Czerwony

def format_to_waybar(text, alt="", class_name="", percentage=-1):
    """
    Formatuj dane do standardu JSON dla modułu 'custom' w Waybar.
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
    Zwraca odpowiedni symbol fontu dla profesji lub podzespołu.
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
    Tworzy tekstowy pasek postępu (np. ▰▰▰▱▱).
    """
    if total <= 0: return "▱" * width
    percent = (current / total)
    filled = int(width * min(max(percent, 0), 1))
    bar = "▰" * filled + "▱" * (width - filled)
    return bar