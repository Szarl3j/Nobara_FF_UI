from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PySide6.QtCore import Qt


class QuestLogWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Główny układ z marginesami, aby ramka nie dotykała krawędzi ekranu
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Kontener dla stylizacji (to tutaj ląduje Twój CSS)
        self.container = QWidget()
        self.container.setObjectName("quest_container")

        # Stylizacja zgodnie z Twoimi wymaganiami
        self.container.setStyleSheet("""
            QWidget#quest_container {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                          stop:0 rgba(40, 40, 40, 0.9), 
                                          stop:1 rgba(20, 20, 20, 0.9));
                border: 2px solid #c2a661;
                border-radius: 0px 15px 0px 15px;
            }
        """)

        container_layout = QHBoxLayout(self.container)
        container_layout.setContentsMargins(15, 8, 15, 8)
        container_layout.setSpacing(10)

        # Ikona zadania (Wykrzyknik / Symbol z Twojego JSON)
        self.icon_label = QLabel("\ue06f")  # Ikona domyślna
        self.icon_label.setStyleSheet("""
            color: #f0e68c;
            font-size: 18px;
            font-weight: bold;
        """)

        # Treść zadania
        self.quest_text = QLabel("Initializing Quest Log...")
        self.quest_text.setStyleSheet("""
            color: #f0e68c;
            font-family: 'Optimus Princeps', 'Cinzel';
            font-size: 14px;
            font-weight: bold;
        """)
        self.quest_text.setWordWrap(True)

        container_layout.addWidget(self.icon_label)
        container_layout.addWidget(self.quest_text)

        self.layout.addWidget(self.container)
        self.setFixedHeight(60)  # Stała wysokość, aby nie "skakał" przy zmianie tekstu

    def update_quest(self, text):
        """Aktualizuje tekst zadania. Możesz tu też dodać parsowanie ikony."""
        if not text:
            return

        # Jeśli tekst zawiera ikonę unicode (jak w Twoim JSON), oddzielamy ją
        if len(text) > 1 and text[0].isprintable() and ord(text[0]) > 1000:
            self.icon_label.setText(text[0])
            self.quest_text.setText(text[1:].strip())
        else:
            self.quest_text.setText(text)