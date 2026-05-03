import os
import shutil
import psutil


def set_gil_icons():
    # Ścieżka do Twojej ikonki
    ICON_SOURCE = os.path.abspath("assets/icons/gil.png")

    if not os.path.exists(ICON_SOURCE):
        print(f"BŁĄD: Nie znaleziono ikony w {ICON_SOURCE}")
        return

    # Pobierz wszystkie zamontowane partycje
    partitions = psutil.disk_partitions()

    for p in partitions:
        # Interesują nas tylko dyski fizyczne (pominąć systemy plików jak /proc czy /dev)
        if 'loop' in p.device or not p.mountpoint.startswith('/'):
            continue

        target_path = os.path.join(p.mountpoint, ".DirIcon")

        try:
            # Próbujemy skopiować ikonę jako ukryty plik .DirIcon
            shutil.copy2(ICON_SOURCE, target_path)
            print(f"Sukces: Ikonka Gil ustawiona dla {p.mountpoint}")
        except PermissionError:
            print(f"Brak uprawnień dla {p.mountpoint} - spróbuj odpalić z sudo.")
        except Exception as e:
            print(f"Nie udało się ustawić ikony dla {p.mountpoint}: {e}")


if __name__ == "__main__":
    set_gil_icons()