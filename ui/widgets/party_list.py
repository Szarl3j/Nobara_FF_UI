from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from modules.alliance.alliance_a_discord.activity_store import get_activity
from modules.alliance.alliance_b_system.metrics import get_metrics
from modules.alliance.alliance_c_apps.running_apps import get_running_apps


class PartyPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.labels = []

        layout = QVBoxLayout()

        self.title = QLabel("FULL PARTY")
        layout.addWidget(self.title)

        for _ in range(24):
            label = QLabel("-")
            self.labels.append(label)
            layout.addWidget(label)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                background: rgba(10, 10, 10, 180);
                color: #d4c8a8;
                border: 1px solid #7a1f1f;
                border-radius: 10px;
                padding: 6px;
            }

            QLabel {
                font-size: 12px;
            }
        """)

    def refresh(self):
        rows = []

        activity = get_activity().get("activity", [])[:8]
        for item in activity:
            name = item.get("name", "Unknown")
            glow = item.get("glow", False)
            rows.append(f"A  {'✦ ' if glow else ''}{name}")

        while len(rows) < 8:
            rows.append("A  -")

        system = get_metrics()
        rows.extend([
            f"B  CPU {system['cpu']}%",
            f"B  GPU {system['gpu']['usage_percent']}%",
            f"B  GPU TEMP {system['gpu']['temperature']}°C",
            f"B  RAM {system['ram']['used_gb']}/{system['ram']['total_gb']}GB",
            f"B  DISK FREE {system['disk']['free_gb']}GB",
            f"B  NET ↓{system['network']['recv_mb']}MB",
            f"B  NET ↑{system['network']['sent_mb']}MB",
            "B  SYS OK"
        ])

        apps = get_running_apps()
        for app in apps[:8]:
            rows.append(f"C  {app}")

        for label, text in zip(self.labels, rows):
            label.setText(text)