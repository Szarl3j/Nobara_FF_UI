from datetime import datetime, timezone

from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt


class GameClock(QWidget):
    def __init__(self, compact=False):
        super().__init__()

        self.compact = compact

        self.lt_label = QLabel()
        self.st_label = QLabel()
        self.et_label = QLabel()

        for label in [self.lt_label, self.st_label, self.et_label]:
            label.setAlignment(Qt.AlignCenter)

        layout = QHBoxLayout()
        layout.addWidget(self.lt_label)

        if not compact:
            layout.addWidget(self.st_label)
            layout.addWidget(self.et_label)

        layout.setContentsMargins(10, 4, 10, 4)
        layout.setSpacing(10)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                background: rgba(5, 5, 8, 220);
                border: 1px solid #c9a86a;
                border-radius: 0px;
            }

            QLabel {
                color: #f5e6b8;
                font-size: 15px;
                font-weight: bold;
                border: none;
            }
        """)

    def refresh(self):
        now = datetime.now()
        utc = datetime.now(timezone.utc)

        lt = now.strftime("%H:%M")
        st = utc.strftime("%H:%M")

        et_hour = (now.hour * 3) % 24
        et = f"{et_hour:02d}:{now.minute:02d}"

        self.lt_label.setText(f"LT {lt}")

        if not self.compact:
            self.st_label.setText(f"ST {st}")
            self.et_label.setText(f"ET {et}")