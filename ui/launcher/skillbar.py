import subprocess

from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout
from PySide6.QtCore import QSize

from core.paths import HOTBAR_CONFIG_FILE, HUD_LAYOUT_CONFIG_FILE
from core.state import load_json
from core.sound import play
from core.icons import get_qicon


DEFAULT_HUD_LAYOUT = {
    "bottom_bar": {
        "skill_button_size": 64,
        "skill_icon_size": 36,
        "skill_columns": 6,
        "font_size": 14
    }
}

DEFAULT_HOTBAR = {
    "columns": 6,
    "sound_on_click": "Duty Pop",
    "slots": [
        {"name": "Steam", "command": "steam", "icon": "Warrior.png"},
        {"name": "Discord", "command": "launch-discord", "icon": "Bard.png"},
        {"name": "Firefox", "command": "launch-browser", "icon": "Pictomancer.png"},
        {"name": "Terminal", "command": "kitty", "icon": "BlackMage.png"},
        {"name": "Files", "command": "dolphin", "icon": "Carpenter.png"},
        {"name": "HUD", "command": "hud-toggle", "icon": "Astrologian.png"}
    ]
}


class SkillBar(QWidget):
    def __init__(self):
        super().__init__()

        hud_settings = load_json(
            HUD_LAYOUT_CONFIG_FILE,
            DEFAULT_HUD_LAYOUT
        ).get("bottom_bar", DEFAULT_HUD_LAYOUT["bottom_bar"])

        self.button_size = hud_settings.get("skill_button_size", 64)
        self.icon_size = hud_settings.get("skill_icon_size", 36)
        self.font_size = hud_settings.get("font_size", 14)

        self.layout = QGridLayout()
        self.layout.setSpacing(4)
        self.setLayout(self.layout)

        self.sound_on_click = "Duty Pop"

        self.load_buttons()

        self.setStyleSheet(f"""
            QWidget {{
                background: rgba(10, 10, 10, 180);
                border: 1px solid #7a1f1f;
                border-radius: 10px;
                padding: 6px;
            }}

            QPushButton {{
                background: rgba(35, 20, 20, 220);
                color: #d4c8a8;
                border: 1px solid #c9a86a;
                border-radius: 6px;
                padding: 4px;
                min-width: {self.button_size}px;
                min-height: {self.button_size}px;
                max-width: {self.button_size}px;
                max-height: {self.button_size}px;
                font-size: {self.font_size}px;
            }}

            QPushButton:hover {{
                background: rgba(122, 31, 31, 230);
                color: white;
                border: 1px solid #ffd700;
            }}
        """)

    def load_buttons(self):
        hotbar = load_json(HOTBAR_CONFIG_FILE, DEFAULT_HOTBAR)

        slots = hotbar.get("slots", DEFAULT_HOTBAR["slots"])
        columns = hotbar.get("columns", DEFAULT_HOTBAR["columns"])
        self.sound_on_click = hotbar.get("sound_on_click", "Duty Pop")

        for index, slot in enumerate(slots):
            name = slot.get("name", "App")
            command = slot.get("command", "")
            icon_name = slot.get("icon", "")

            button = QPushButton(name)
            button.setIconSize(QSize(self.icon_size, self.icon_size))

            if icon_name:
                button.setIcon(get_qicon(icon_name))

            button.clicked.connect(
                lambda checked=False, cmd=command: self.launch(cmd)
            )

            row = index // columns
            col = index % columns

            self.layout.addWidget(button, row, col)

    def launch(self, command):
        if not command:
            return

        play(self.sound_on_click)
        subprocess.Popen(command, shell=True)