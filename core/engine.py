import sys
import os
import json
import time
import psutil
import threading
import subprocess
import random

# --- SEKCJA NAPRAWCZA IMPORTÓW ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

# Poprawiony import: funkcja w ff_utils nazywa się format_gil_value
try:
    from ff_utils import get_eorzea_time, format_gil_value as format_gil

    print(">>> Import: Załadowano ff_utils.py")
except ImportError as e:
    print(f">>> KRYTYCZNY BŁĄD: Problem z importem z ff_utils.py: {e}")
    sys.exit(1)

# Import Managera Alliance - upewnij się, że klasa w ff_alliance.py ma tę nazwę
try:
    from ff_alliance import AllianceManager
except ImportError:
    # Fallback jeśli klasa nazywa się inaczej (np. FFAllianceGroup)
    from ff_alliance import FFAllianceGroup as AllianceManager

# BEZPIECZNIK D-BUS
try:
    from notifications import NotificationListener

    HAS_DBUS = True
except (ImportError, ModuleNotFoundError):
    HAS_DBUS = False


    class NotificationListener:
        def __init__(self, callback): pass

        def start(self): pass

# Ścieżki do plików
BASE_DIR = os.path.dirname(CURRENT_DIR)
DATA_PATH = os.path.join(BASE_DIR, "data.json")
TODO_PATH = os.path.expanduser("~/todo.txt")
SOUNDS_DIR = os.path.join(BASE_DIR, "assets", "sounds")


class EorzeaEngine:
    def __init__(self):
        self.alliance = AllianceManager()
        self.allowed_sounds = [
            "Message.mp3",
            "notification.mp3",
            "ffxiv-message-2.mp3"
        ]
        self.current_sound = random.choice(self.allowed_sounds) if self.allowed_sounds else None
        self.last_messenger = "Searching..."
        self.rotate_sounds_loop()

    def rotate_sounds_loop(self):
        """Zmienia aktywny dźwięk powiadomienia co 5 minut."""
        if self.allowed_sounds:
            self.current_sound = random.choice(self.allowed_sounds)
            print(f">>> Rotacja: Aktywny dźwięk to teraz: {self.current_sound}")

        timer = threading.Timer(300, self.rotate_sounds_loop)
        timer.daemon = True
        timer.start()

    def handle_notification(self, sender):
        """Obsługa powiadomień systemowych (np. Discord)."""
        self.last_messenger = sender
        if self.current_sound:
            sound_path = os.path.join(SOUNDS_DIR, self.current_sound)
            player = "mpv --no-video" if os.name != 'nt' else "ffplay -nodisp -autoexit"
            if os.path.exists(sound_path):
                subprocess.Popen(f"{player} \"{sound_path}\"", shell=True,
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def get_quests(self):
        """Pobiera zadania z ~/todo.txt."""
        if not os.path.exists(TODO_PATH): return "No Active Quests"
        try:
            with open(TODO_PATH, 'r', encoding='utf-8') as f:
                lines = [l.strip() for l in f.readlines() if l.strip()]
            return lines[0] if lines else "Journal Empty"
        except:
            return "Quest Journal Error"

    def run(self):
        if HAS_DBUS:
            listener = NotificationListener(self.handle_notification)
            threading.Thread(target=listener.start, daemon=True).start()

        print("--- EORZEA RAID ENGINE ONLINE (24 SLOTS) ---")

        while True:
            # Pobieranie danych
            group_a = self.alliance.get_social_info()
            group_b = self.alliance.get_music_info()
            group_c = self.alliance.get_system_stats()

            # Obliczanie wolnego miejsca na dysku jako Gil
            # Dzielimy przez 100, aby uzyskać fajną wartość "grową"
            free_space_mb = psutil.disk_usage('/').free / (1024 * 1024)
            gil_val = int(free_space_mb / 100)

            full_data = {
                "et": get_eorzea_time(),
                "quest": f"\ue06f {self.get_quests()}",
                "gil": format_gil(gil_val),
                "party_a": group_a,
                "alliance_b": group_b,
                "alliance_c": group_c,
                "last_messenger": self.last_messenger,
                "raid_status": "In Duty",
                "last_update": time.strftime("%H:%M:%S")
            }

            # Zapis do JSON
            try:
                tmp_path = DATA_PATH + ".tmp"
                with open(tmp_path, 'w', encoding='utf-8') as f:
                    json.dump(full_data, f, indent=4)

                if os.name == 'nt' and os.path.exists(DATA_PATH):
                    os.remove(DATA_PATH)
                os.rename(tmp_path, DATA_PATH)
            except Exception as e:
                print(f"Błąd zapisu JSON: {e}")

            time.sleep(1)


if __name__ == "__main__":
    engine = EorzeaEngine()
    engine.run()