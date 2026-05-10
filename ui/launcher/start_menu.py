import subprocess

from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

from core.paths import ICONS_DIR, HUD_LAYOUT_CONFIG_FILE
from core.state import load_json
from core.sound import play


DEFAULT_LAYOUT = {
    "bottom_bar": {
        "start_button_size": 110
    }
}


class StartMenuButton(QWidget):
    def __init__(self):
        super().__init__()

        settings = load_json(HUD_LAYOUT_CONFIG_FILE, DEFAULT_LAYOUT).get(
            "bottom_bar",
            DEFAULT_LAYOUT["bottom_bar"]
        )

        size = settings.get("start_button_size", 110)

        self.button = QPushButton("")

        start_icon = ICONS_DIR / "start_menu.png"

        if start_icon.exists():
            self.button.setIcon(QIcon(str(start_icon)))

        self.button.setIconSize(QSize(size - 28, size - 28))
        self.button.setFixedSize(size, size)

        self.button.clicked.connect(self.open_menu)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

        self.setStyleSheet(f"""
            QPushButton {{
                background: rgba(25, 10, 10, 230);
                border: 2px solid #c9a86a;
                border-radius: {int(size / 5)}px;
                padding: 10px;
            }}

            QPushButton:hover {{
                background: rgba(122, 31, 31, 240);
                border: 2px solid #ffd700;
            }}

            QPushButton:pressed {{
                background: rgba(180, 40, 40, 255);
            }}
        """)

    def open_menu(self):
        play("Duty Pop")
        subprocess.Popen("rofi -show drun", shell=True)