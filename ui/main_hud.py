import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from core.paths import (
    ensure_directories,
    UI_STATE_FILE,
    HUD_LAYOUT_CONFIG_FILE
)
from core.state import load_json, save_json

from ui.hud_bottom_bar import HUDBottomBar

from ui.widgets.limit_break import LimitBreakWidget
from ui.widgets.game_clock import GameClock
from ui.widgets.gil_disk_widget import GilDiskWidget

from ui.widgets.discord_panel import DiscordPanel
from ui.widgets.system_panel import SystemPanel
from ui.widgets.apps_panel import AppsPanel
from ui.widgets.quest_log import QuestLogWidget
from ui.widgets.draggable_panel import DraggablePanel


DEFAULT_LAYOUT = {
    "discord": {"x": 60, "y": 220, "w": 280, "h": 320},
    "system": {"x": 360, "y": 220, "w": 300, "h": 320},
    "apps": {"x": 680, "y": 220, "w": 280, "h": 320},
    "quest": {"x": 980, "y": 220, "w": 320, "h": 320}
}

DEFAULT_HUD_LAYOUT = {
    "bottom_bar": {
        "height": 130
    }
}


class MainHUD:
    def __init__(self):
        self.widgets = []

        self.layout_state = load_json(
            UI_STATE_FILE,
            {"panels": DEFAULT_LAYOUT}
        )

        hud_config = load_json(
            HUD_LAYOUT_CONFIG_FILE,
            DEFAULT_HUD_LAYOUT
        )

        self.bottom_bar_height = (
            hud_config
            .get("bottom_bar", {})
            .get("height", 130)
        )

        self.limit_break = LimitBreakWidget()
        self.clock = GameClock(compact=False)
        self.gil_disk = GilDiskWidget()
        self.bottom_bar = HUDBottomBar()

        self.discord_panel = DraggablePanel(DiscordPanel(), "discord")
        self.system_panel = DraggablePanel(SystemPanel(), "system")
        self.apps_panel = DraggablePanel(AppsPanel(), "apps")
        self.quest_log = DraggablePanel(QuestLogWidget(), "quest")

        self.movable_panels = [
            self.discord_panel,
            self.system_panel,
            self.apps_panel,
            self.quest_log
        ]

        for panel in self.movable_panels:
            panel.on_layout_changed = self.save_layout

        self.widgets.extend([
            self.limit_break,
            self.clock,
            self.gil_disk,
            self.bottom_bar,
            *self.movable_panels
        ])

        self.position_widgets()

        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(2000)

        self.refresh()

    def position_widgets(self):
        screen = QApplication.primaryScreen().availableGeometry()

        # Limit Break — lewy górny róg, od krawędzi
        self.limit_break.move(0, 0)
        self.limit_break.show()

        # Czas LT/ST/ET — prawy górny róg, od krawędzi
        self.clock.adjustSize()
        self.clock.move(
            screen.width() - self.clock.width(),
            0
        )
        self.clock.show()

        # Dolny pasek
        self.bottom_bar.setGeometry(
            0,
            screen.height() - self.bottom_bar_height,
            screen.width(),
            self.bottom_bar_height
        )
        self.bottom_bar.show()

        # Gil/Dysk — prawy dolny róg nad paskiem
        self.gil_disk.move(
            screen.width() - self.gil_disk.width() - 8,
            screen.height() - self.bottom_bar_height - self.gil_disk.height() - 8
        )
        self.gil_disk.show()

        panel_layouts = self.layout_state.get(
            "panels",
            DEFAULT_LAYOUT
        )

        for panel in self.movable_panels:
            geo = panel_layouts.get(
                panel.panel_id,
                DEFAULT_LAYOUT[panel.panel_id]
            )

            panel.setGeometry(
                geo.get("x", DEFAULT_LAYOUT[panel.panel_id]["x"]),
                geo.get("y", DEFAULT_LAYOUT[panel.panel_id]["y"]),
                geo.get("w", DEFAULT_LAYOUT[panel.panel_id]["w"]),
                geo.get("h", DEFAULT_LAYOUT[panel.panel_id]["h"])
            )

            panel.show()

    def save_layout(self):
        panels = {}

        for panel in self.movable_panels:
            panels[panel.panel_id] = {
                "x": panel.x(),
                "y": panel.y(),
                "w": panel.width(),
                "h": panel.height()
            }

        save_json(
            UI_STATE_FILE,
            {"panels": panels}
        )

    def refresh(self):
        for widget in self.widgets:
            if hasattr(widget, "refresh"):
                widget.refresh()


if __name__ == "__main__":
    ensure_directories()

    app = QApplication(sys.argv)

    hud = MainHUD()

    sys.exit(app.exec())