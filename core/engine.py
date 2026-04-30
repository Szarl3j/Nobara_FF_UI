import json
import time
import os
import psutil
from alliance import AllianceManager
from utils import get_eorzea_time

# Ścieżki
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data.json")
TODO_PATH = os.path.expanduser("~/todo.txt")


class EorzeaEngine:
    def __init__(self):
        self.alliance = AllianceManager()

    def get_quests(self):
        if not os.path.exists(TODO_PATH): return "No Quests"
        with open(TODO_PATH, 'r') as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
        return lines[0] if lines else "Journal Empty"

    def run(self):
        while True:
            # Budowanie paczki danych
            full_data = {
                "et": get_eorzea_time(),
                "quest": self.get_quests(),
                "lb": self.alliance.get_system_stats(),  # Lista C
                "music": self.alliance.get_music_info(),  # Lista B
                "party_a": self.alliance.get_discord_data()  # Lista A
            }

            # Zapis do JSON dla Waybara
            with open(DATA_PATH, 'w') as f:
                json.dump(full_data, f, indent=4)

            time.sleep(1)  # Odświeżanie co sekundę


if __name__ == "__main__":
    engine = EorzeaEngine()
    engine.run()