import sys

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout

from ui.widgets.limit_break import LimitBreakWidget
from ui.widgets.discord_panel import DiscordPanel
from ui.widgets.system_panel import SystemPanel
from ui.widgets.apps_panel import AppsPanel
from ui.widgets.quest_log import QuestLogWidget
from ui.launcher.skillbar import SkillBar


class MainHUD(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nobara FFXIV HUD")

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.discord_panel = DiscordPanel()
        self.system_panel = SystemPanel()
        self.apps_panel = AppsPanel()
        self.limit_break = LimitBreakWidget()
        self.quest_log = QuestLogWidget()
        self.skillbar = SkillBar()

        layout = QHBoxLayout()
        layout.addWidget(self.discord_panel)
        layout.addWidget(self.system_panel)
        layout.addWidget(self.apps_panel)
        layout.addWidget(self.limit_break)
        layout.addWidget(self.quest_log)
        layout.addWidget(self.skillbar)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(2000)

        self.refresh()

    def refresh(self):
        self.discord_panel.refresh()
        self.system_panel.refresh()
        self.apps_panel.refresh()
        self.limit_break.refresh()
        self.quest_log.refresh()


if __name__ == "__main__":
    from core.paths import ensure_directories

    ensure_directories()

    app = QApplication(sys.argv)

    hud = MainHUD()
    hud.move(80, 80)
    hud.show()

    sys.exit(app.exec())