import shutil

from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from core.icons import get_pixmap


class GilDiskWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.icon = QLabel()
        self.icon.setPixmap(get_pixmap("gil", 22))

        self.label = QLabel("0 GB")

        layout = QHBoxLayout()
        layout.addWidget(self.icon)
        layout.addWidget(self.label)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(6)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                background: rgba(0, 0, 0, 225);
                border: 1px solid #ffd700;
                border-radius: 10px;
            }

            QLabel {
                color: #fff2a8;
                font-size: 14px;
                font-weight: bold;
                border: none;
            }
        """)

        self.setFixedSize(145, 42)

    def refresh(self):
        usage = shutil.disk_usage("/")
        free_gb = round(usage.free / 1024 / 1024 / 1024, 1)
        self.label.setText(f"{free_gb} GB")