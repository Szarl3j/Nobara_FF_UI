from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QProgressBar

from core.paths import THRESHOLDS_CONFIG_FILE
from core.state import load_json
from core.system_monitor import collect_system_status
from core.sound import play


DEFAULT_THRESHOLDS = {
    "limit_break": {
        "enabled": True,
        "gpu_temp_warning": 80,
        "gpu_temp_critical": 92,
        "gpu_usage_warning": 85,
        "gpu_usage_critical": 96,
        "cpu_usage_warning": 80,
        "cpu_usage_critical": 95,
        "ram_usage_warning": 80,
        "ram_usage_critical": 94,
        "play_warning_sound": True,
        "warning_sound": "ffxiv-message-2",
        "critical_sound": "Duty Pop"
    }
}


class LimitBreakWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.warning_played = False
        self.critical_played = False

        self.title = QLabel("LIMIT BREAK")
        self.gpu_bar = QProgressBar()
        self.cpu_bar = QProgressBar()
        self.ram_bar = QProgressBar()

        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(QLabel("GPU TEMP"))
        layout.addWidget(self.gpu_bar)
        layout.addWidget(QLabel("CPU"))
        layout.addWidget(self.cpu_bar)
        layout.addWidget(QLabel("RAM"))
        layout.addWidget(self.ram_bar)

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
                color: #ff4444;
                font-weight: bold;
            }

            QProgressBar {
                height: 12px;
                border: 1px solid #c9a86a;
                border-radius: 6px;
                background: #111;
                color: white;
            }

            QProgressBar::chunk {
                background: #ffd700;
                border-radius: 6px;
            }
        """)

    def refresh(self):
        thresholds = load_json(
            THRESHOLDS_CONFIG_FILE,
            DEFAULT_THRESHOLDS
        ).get("limit_break", DEFAULT_THRESHOLDS["limit_break"])

        if not thresholds.get("enabled", True):
            self.title.setText("LIMIT BREAK DISABLED")
            return

        data = collect_system_status()

        gpu_temp = data["gpu"]["temperature"]
        gpu_usage = data["gpu"]["usage_percent"]
        cpu = int(data["cpu"])
        ram_percent = int(data["ram"]["percent"])

        self.gpu_bar.setValue(min(gpu_temp, 100))
        self.cpu_bar.setValue(cpu)
        self.ram_bar.setValue(ram_percent)

        warning = (
            gpu_temp >= thresholds["gpu_temp_warning"]
            or gpu_usage >= thresholds["gpu_usage_warning"]
            or cpu >= thresholds["cpu_usage_warning"]
            or ram_percent >= thresholds["ram_usage_warning"]
        )

        critical = (
            gpu_temp >= thresholds["gpu_temp_critical"]
            or gpu_usage >= thresholds["gpu_usage_critical"]
            or cpu >= thresholds["cpu_usage_critical"]
            or ram_percent >= thresholds["ram_usage_critical"]
        )

        if critical:
            self.title.setText("LIMIT BREAK III")
            if not self.critical_played and thresholds.get("play_warning_sound", True):
                play(thresholds.get("critical_sound", "Duty Pop"))
                self.critical_played = True

        elif warning:
            self.title.setText("LIMIT BREAK READY")
            if not self.warning_played and thresholds.get("play_warning_sound", True):
                play(thresholds.get("warning_sound", "ffxiv-message-2"))
                self.warning_played = True

        else:
            self.title.setText("LIMIT BREAK")
            self.warning_played = False
            self.critical_played = False