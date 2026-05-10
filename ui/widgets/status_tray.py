import psutil

from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
from core.icons import get_pixmap


class StatusTray(QWidget):
    def __init__(self):
        super().__init__()

        self.net_icon = QLabel()
        self.net_icon.setPixmap(get_pixmap("network", 32))

        self.net_label = QLabel("NET")

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.net_icon)
        self.layout.addWidget(self.net_label)

        self.setLayout(self.layout)

        self.setStyleSheet("""
            QWidget {
                background: rgba(10, 10, 10, 190);
                border: 1px solid #7a1f1f;
                border-radius: 12px;
                padding: 8px;
            }

            QLabel {
                color: #d4c8a8;
                font-size: 16px;
                font-weight: bold;
                border: none;
            }
        """)

    def refresh(self):
        try:
            stats = psutil.net_io_counters()
            recv = round(stats.bytes_recv / 1024 / 1024, 1)
            sent = round(stats.bytes_sent / 1024 / 1024, 1)
            self.net_label.setText(f"↓{recv} ↑{sent}")
        except Exception:
            self.net_label.setText("NET N/A")