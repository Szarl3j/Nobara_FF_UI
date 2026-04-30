import time
import json
import subprocess
from alliance import AllianceManager
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Handler dla pliku todo.txt
class QuestHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if "todo.txt" in event.src_path:
            # Nobara ma mpv domyślnie - używamy go do dźwięku
            subprocess.Popen(["mpv", "--no-video", "assets/sounds/quest_accept.mp3"],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    manager = AllianceManager()

    # Uruchamiamy monitorowanie pliku todo
    event_handler = QuestHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    print("FFXIV HUD Engine Started...")

    try:
        while True:
            # Pobieramy aktualne zadanie z pierwszej linii todo.txt
            try:
                with open("todo.txt", "r") as f:
                    current_quest = f.readline().strip() or "No Active Quest"
            except File_Not_Found_Error:
                current_quest = "Create todo.txt!"

            # Budujemy paczkę danych
            data = {
                "et": manager.get_eorzea_time(),
                "quest": current_quest,
                "alliance_c": manager.get_hardware_stats(),
                "gil": "{:,}".format(psutil.disk_usage('/').free // 100000000),  # Gil jako wolne miejsce
                "lb_level": 3 if psutil.cpu_percent() > 80 else 1
            }

            # Zapisujemy do data.json (Waybar to czyta)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

            time.sleep(1)  # Odświeżanie co sekundę
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()