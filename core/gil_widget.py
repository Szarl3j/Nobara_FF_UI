from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PySide6.QtCore import Qt
from core.set_icons import get_icon

class GilWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Układ wyrównany do prawej (jak w UI gry)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 5, 10, 0)
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignRight)

        # Licznik "pieniędzy" (wolne miejsce na dysku)
        self.amount_label = QLabel("0")
        self.amount_label.setStyleSheet("""
            color: #ffffff;
            font-family: 'JetBrains Mono';
            font-size: 16px;
            font-weight: bold;
            text-shadow: 1px 1px 2px black;
        """)

        # Ikona Gil
        self.icon_label = QLabel()
        self.icon_label.setFixedSize(18, 18)
        self.icon_label.setPixmap(get_icon("gil", 18))

        layout.addWidget(self.amount_label)
        layout.addWidget(self.icon_label)

    def update_value(self, free_gb):
        """
        free_gb: int lub float reprezentujący wolne miejsce.
        Formatujemy to z separatorami tysięcy (np. 1 234)
        """
        formatted_val = "{:,}".format(int(free_gb)).replace(",", " ")
        self.amount_label.setText(formatted_val)