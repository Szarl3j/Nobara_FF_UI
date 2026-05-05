import sys
import json
import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import QTimer, Qt

# Importy wszystkich Twoich modułów z folderu core/
from core.clock_widget import FFXIVClock
from core.ff_alliance import FFAllianceGroup
from core.gil_widget import GilWidget
from core.quest_log import QuestLogWidget
from core.limit_break import LimitBreakWidget
from core.ff_utils import get_eorzea_time, format_gil_value

# Ścieżki lokalne
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data.json")


class AllianceOverlay(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # Główny Timer Odświeżania (1 sekunda)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)

    def init_ui(self):
        # Konfiguracja okna Overlay
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool |
            Qt.WindowDoesNotAcceptFocus
        )
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Główny kontener pionowy
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(25, 25, 25, 25)
        self.main_layout.setSpacing(15)

        # --- GÓRNA SEKCJA (Quest Log + Zegar) ---
        self.top_section = QHBoxLayout()
        self.quest_log = QuestLogWidget()
        self.clock = FFXIVClock()

        self.top_section.addWidget(self.quest_log, alignment=Qt.AlignLeft)
        self.top_section.addStretch()
        self.top_section.addWidget(self.clock, alignment=Qt.AlignRight)
        self.main_layout.addLayout(self.top_section)

        # --- SEKCJA LIMIT BREAK ---
        self.lb_bar = LimitBreakWidget()
        self.main_layout.addWidget(self.lb_bar, alignment=Qt.AlignCenter)

        # --- ŚRODKOWA SEKCJA (Alliance A, B, C) ---
        self.alliance_layout = QHBoxLayout()
        self.alliance_layout.setSpacing(40)

        self.group_a = FFAllianceGroup("A")
        self.group_b = FFAllianceGroup("B")
        self.group_c = FFAllianceGroup("C")

        self.alliance_layout.addWidget(self.group_a)
        self.alliance_layout.addWidget(self.group_b)
        self.alliance_layout.addWidget(self.group_c)
        self.main_layout.addLayout(self.alliance_layout)

        # Spacer wypychający Gil na dół
        self.main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # --- DOLNA SEKCJA (Gil / Status) ---
        self.gil_display = GilWidget()
        self.main_layout.addWidget(self.gil_display, alignment=Qt.AlignRight)

        # Globalny styl fontów
        self.setStyleSheet("""
            * {
                font-family: 'Optimus Princeps', 'Cinzel', 'JetBrains Mono';
                text-shadow: 2px 2px 3px black;
            }
        """)

        # Ustawienia rozmiaru okna (dopasuj do rozdzielczości ekranu)
        self.setGeometry(0, 0, 1200, 800)

    def update_data(self):
        """Pobiera dane z JSON i rozsyła do widgetów."""
        if not os.path.exists(DATA_PATH):
            return

        try:
            with open(DATA_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 1. Aktualizacja Quest Logu
            if "quest" in data:
                self.quest_log.update_quest(data["quest"])

            # 2. Aktualizacja Alliance (Drużyny)
            if "party_a" in data:
                self.group_a.update_members(data["party_a"])
            if "alliance_b" in data:
                self.group_b.update_members(data["alliance_b"])
            if "alliance_c" in data:
                self.group_c.update_members(data["alliance_c"])

            # 3. Aktualizacja Limit Break (na podstawie Alliance C - CPU Load)
            # W Twoim JSON Alliance C[0] to CPU_CORE. Jeśli HP = 100, obciążenie = 0.
            if "alliance_c" in data and len(data["alliance_c"]) > 0:
                cpu_hp = float(data["alliance_c"][0].get("hp", 100))
                load_val = 100 - cpu_hp
                self.lb_bar.update_lb(load_val)

            # 4. Aktualizacja Gil (używamy utila do formatowania)
            if "gil" in data:
                formatted_gil = format_gil_value(data["gil"])
                self.gil_display.update_value(formatted_gil)

            # 5. Aktualizacja Zegara (Prawdziwe ET z utils zamiast statycznego z JSON)
            if hasattr(self.clock, 'et_val'):
                self.clock.et_val.setText(get_eorzea_time())

        except Exception as e:
            print(f"HUD Update Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Tworzymy i pokazujemy Overlay
    overlay = AllianceOverlay()
    overlay.show()

    # Nobara / Linux Fix (wymuszenie bycia nad innymi oknami)
    os.system("wmctrl -r 'AllianceOverlay' -b add,sticky,above 2>/dev/null")

    sys.exit(app.exec())