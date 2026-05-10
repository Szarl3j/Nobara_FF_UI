from PySide6.QtWidgets import QWidget, QHBoxLayout

from core.paths import HUD_LAYOUT_CONFIG_FILE
from core.state import load_json

from ui.launcher.start_menu import StartMenuButton
from ui.launcher.skillbar import SkillBar
from ui.widgets.game_clock import GameClock


DEFAULT_LAYOUT = {
    "bottom_bar": {
        "height": 130,
        "spacing": 14
    }
}


class HUDBottomBar(QWidget):
    def __init__(self):
        super().__init__()

        settings = load_json(HUD_LAYOUT_CONFIG_FILE, DEFAULT_LAYOUT).get(
            "bottom_bar",
            DEFAULT_LAYOUT["bottom_bar"]
        )

        self.height = settings.get("height", 130)
        spacing = settings.get("spacing", 14)

        self.start_menu = StartMenuButton()
        self.skillbar = SkillBar()
        self.lt_clock = GameClock(compact=True)

        layout = QHBoxLayout()
        layout.addWidget(self.start_menu)
        layout.addWidget(self.skillbar)
        layout.addStretch()
        layout.addWidget(self.lt_clock)

        layout.setContentsMargins(18, 8, 18, 14)
        layout.setSpacing(spacing)

        self.setLayout(layout)
        self.setFixedHeight(self.height)

        self.setStyleSheet("""
            QWidget {
                background: rgba(5, 5, 8, 210);
                border-top: 2px solid #7a1f1f;
            }
        """)

    def refresh(self):
        self.lt_clock.refresh()