import time
import math


def get_eorzea_time():
    """
    Oblicza aktualny czas Eorzea (ET) na podstawie czasu rzeczywistego.
    1 godzina ET = 175 sekund rzeczywistych.
    """
    # Stała przeliczeniowa: 1440 minut Eorzei to 70 minut rzeczywistych
    EORZEA_MULTIPLIER = 1440 / 70

    # Pobieramy czas Unix i przeliczamy na minuty Eorzei
    epoch_time = time.time()
    eorzea_total_minutes = epoch_time * EORZEA_MULTIPLIER / 60

    eorzea_minutes = int(eorzea_total_minutes % 60)
    eorzea_hours = int((eorzea_total_minutes / 60) % 24)

    return f"{eorzea_hours:02d}:{eorzea_minutes:02d}"


def format_gil_value(value):
    """Formatuje surową liczbę lub string na format z przerwami (np. 31 645)."""
    try:
        # Usuwamy istniejące spacje i formatujemy na nowo
        clean_val = str(value).replace(" ", "").replace(",", "")
        return "{:,}".format(int(clean_val)).replace(",", " ")
    except (ValueError, TypeError):
        return value


def get_load_color(value):
    """Zwraca kolor w zależności od obciążenia (HP w Twoim przypadku)."""
    if value > 70: return "#3fb361"  # Zielony (Bezpiecznie)
    if value > 30: return "#c2a661"  # Żółty (Średnio)
    return "#ff3300"  # Czerwony (Krytycznie)