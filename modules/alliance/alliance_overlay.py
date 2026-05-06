from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PySide6.QtCore import Qt
import json
from pathlib import Path
import sys

BASE_DIR = Path.home() / "Nobara_FF_UI"
FILE = BASE_DIR / "modules" / "alliance" / "alliance.json"


class AllianceOverlay(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Alliance HUD")

        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout()

        try:
            with open(FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            for key in data:
                name = data[key]["name"]
                count = len(data[key]["members"])

                label = QLabel(f"{name}: {count}")

                label.setStyleSheet("""
                    color: gold;
                    font-size: 18px;
                    background: rgba(0,0,0,150);
                    padding: 6px;
                """)

                layout.addWidget(label)

        except Exception:
            layout.addWidget(QLabel("Alliance Error"))

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = AllianceOverlay()
    window.show()

    sys.exit(app.exec())