import os
import random
import psutil


# --- LOGIKA DANYCH (Dostępna dla engine.py bez PySide6) ---

class AllianceManager:
    """Klasa zarządzająca logiką danych dla 24 slotów (A, B, C)."""

    def __init__(self):
        self.jobs = ["WAR", "PLD", "DRK", "GNB", "WHM", "SCH", "AST", "SGE",
                     "MNK", "DRG", "NIN", "SAM", "RPR", "VPR", "BRD", "MCH",
                     "DNC", "BLM", "SMN", "RDM", "PCT"]

    def get_social_info(self):
        """Grupa A: Symulacja statusu znajomych/systemu."""
        names = ["System_Kernel", "Wayland_Srv", "Dbus_Monitor", "Network_Mgr", "Pipewire_Audio", "Docker_Daemon",
                 "Xwayland", "Nvidia_Mod"]
        return [{"name": n, "job": random.choice(self.jobs), "hp": random.randint(80, 100)} for n in names]

    def get_music_info(self):
        """Grupa B: Informacje o audio / odtwarzaczu."""
        # Tu można wpiąć playerctl w przyszłości
        return [
            {"name": "Susan Calloway", "job": "BRD", "hp": 100},
            {"name": "Answers - FFXIV", "job": "NONE", "hp": 45},  # Postęp piosenki
            {"name": "Volume_Lvl", "job": "DNC", "hp": 70}
        ] + [{"name": "Slot_Empty", "job": "NONE", "hp": 0} for _ in range(5)]

    def get_system_stats(self):
        """Grupa C: Realne statystyki sprzętowe."""
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        temp = 40  # Statycznie, chyba że masz zainstalowane lm-sensors

        return [
            {"name": "CPU_LOAD", "job": "GNB", "hp": 100 - cpu},
            {"name": "RAM_USAGE", "job": "AST", "hp": 100 - ram},
            {"name": "GPU_TEMP", "job": "BLM", "hp": 100 - temp},
        ] + [{"name": "Srv_Thread", "job": "NIN", "hp": 100} for _ in range(5)]


# --- LOGIKA UI (Ładowana tylko jeśli PySide6 jest dostępne) ---

try:
    from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QProgressBar
    from PySide6.QtCore import Qt
    from core.set_icons import get_job_icon


    class FFMemberWidget(QWidget):
        def __init__(self, name, job, hp, parent=None):
            super().__init__(parent)
            layout = QHBoxLayout(self)
            layout.setContentsMargins(0, 2, 0, 2)
            layout.setSpacing(8)

            # Ikona Klasy
            self.icon_lbl = QLabel()
            self.icon_lbl.setPixmap(get_job_icon(job, 18))

            # Nazwa
            self.name_lbl = QLabel(name[:12])
            self.name_lbl.setStyleSheet("color: white; font-size: 12px; font-weight: bold;")
            self.name_lbl.setFixedWidth(90)

            # Pasek HP
            self.hp_bar = QProgressBar()
            self.hp_bar.setRange(0, 100)
            self.hp_bar.setValue(hp)
            self.hp_bar.setTextVisible(False)
            self.hp_bar.setFixedHeight(8)

            color = "#3fb361" if hp > 30 else "#ff3300"
            self.hp_bar.setStyleSheet(f"""
                QProgressBar {{ background: rgba(0,0,0,0.5); border: 1px solid #444; border-radius: 2px; }}
                QProgressBar::chunk {{ background: {color}; }}
            """)

            layout.addWidget(self.icon_lbl)
            layout.addWidget(self.name_lbl)
            layout.addWidget(self.hp_bar)


    class FFAllianceGroup(QWidget):
        def __init__(self, letter, parent=None):
            super().__init__(parent)
            self.layout = QVBoxLayout(self)
            self.layout.setContentsMargins(5, 5, 5, 5)
            self.layout.setSpacing(2)

            self.title = QLabel(f"ALLIANCE {letter}")
            self.title.setStyleSheet("color: #aaa; font-size: 10px; font-weight: bold; margin-bottom: 5px;")
            self.layout.addWidget(self.title)

            self.members_container = QVBoxLayout()
            self.layout.addLayout(self.members_container)

        def update_members(self, members_data):
            # Usuwamy stare widgety
            while self.members_container.count():
                child = self.members_container.takeAt(0)
                if child.widget(): child.widget().deleteLater()

            # Dodajemy nowe
            for m in members_data:
                self.members_container.addWidget(FFMemberWidget(m['name'], m['job'], m['hp']))

except ImportError:
    # Jeśli PySide6 nie ma, te klasy po prostu nie zostaną zdefiniowane,
    # co pozwala engine.py działać bez błędów.
    pass