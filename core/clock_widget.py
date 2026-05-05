from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PySide6.QtCore import QTimer, Qt
from datetime import datetime


class FFXIVClock(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

        # Timer odświeżający zegar co sekundę
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def format_ff_time(self, dt):
        """Format: 10:53 a.m. (małe litery i kropki)"""
        # %I to format 12h, %p to AM/PM
        t_str = dt.strftime("%I:%M %p").lower()
        # Zamiana am/pm na a.m./p.m. i usunięcie zera wiodącego (np. 01:00 -> 1:00)
        return t_str.replace("am", "a.m.").replace("pm", "p.m.").lstrip("0")

    def init_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignRight)

        # Ikona Wi-Fi (zgodnie z obrazkiem)
        self.wifi_label = QLabel("")
        self.wifi_label.setStyleSheet("color: #e5c07b; font-size: 14px;")
        layout.addWidget(self.wifi_label)

        # Funkcja pomocnicza do tworzenia bloków ET/LT/ST
        def create_block(label_text, bg_color):
            container = QHBoxLayout()
            container.setSpacing(5)

            # Etykieta (np. LT) - Styl Cinzel, tło, ciemny tekst
            lbl = QLabel(label_text)
            lbl.setStyleSheet(f"""
                background-color: {bg_color}; color: #2a2a2a;
                font-family: 'Cinzel'; font-weight: bold; font-size: 11px;
                border-radius: 2px; padding: 0px 4px;
            """)

            # Wartość czasu - Styl JetBrains Mono, jasny tekst z cieniem
            val = QLabel("--:-- --")
            val.setStyleSheet("""
                color: #dcdccc; font-family: 'JetBrains Mono';
                font-size: 14px; text-shadow: 1px 1px 2px black;
            """)

            container.addWidget(lbl)
            container.addWidget(val)
            layout.addLayout(container)
            return val

        # Tworzymy 3 bloki czasu
        self.et_val = create_block("ET", "#e5c07b")  # Złoty
        self.lt_val = create_block("LT", "#c9c9c9")  # Szary
        self.st_val = create_block("ST", "#c9c9c9")  # Szary

        # Strzałka na końcu
        self.arrow = QLabel("")
        self.arrow.setStyleSheet("color: #dcdccc; font-size: 14px;")
        layout.addWidget(self.arrow)

    def update_time(self):
        # LT (Local Time) - zawsze bierze czas z systemu (Nobara/Linux)
        # Będzie on identyczny z Windowsem, jeśli systemy są zsynchronizowane przez sieć.
        now = datetime.now()
        formatted = self.format_ff_time(now)

        self.lt_val.setText(formatted)

        # ET i ST - na razie pokazujemy ten sam czas
        # (W engine.py będziesz mógł dopisać logikę dla Eorzea Time)
        self.et_val.setText(formatted)
        self.st_val.setText(formatted)