import sys
import json
from pathlib import Path

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout
)

BASE_DIR = Path.home() / "Nobara_FF_UI"
DATA_FILE = BASE_DIR / "data.json"


class Overlay(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("FFXIV HUD")

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.label = QLabel("Loading...")

        self.label.setStyleSheet("""
            color: gold;
            font-size: 24px;
            background: rgba(0,0,0,160);
            padding: 12px;
            border-radius: 10px;
        """)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(2000)

        self.update_data()

    def update_data(self):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            text = (
                f"{data['character']}\n"
                f"{data['job']} | {data['world']}\n"
                f"Gil: {data['gil']}"
            )

            self.label.setText(text)

        except Exception:
            self.label.setText("No Data")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    overlay = Overlay()
    overlay.show()

    sys.exit(app.exec())