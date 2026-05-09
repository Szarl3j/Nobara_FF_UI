from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt

from core.icons import get_pixmap


class BasePanel(QWidget):
    def __init__(self, title: str, icon: str = "default"):
        super().__init__()

        self.title_icon = QLabel()
        self.title_icon.setPixmap(get_pixmap(icon, 24))

        self.title = QLabel(title)
        self.title.setObjectName("panelTitle")

        header = QHBoxLayout()
        header.addWidget(self.title_icon)
        header.addWidget(self.title)
        header.addStretch()

        self.layout = QVBoxLayout()
        self.layout.addLayout(header)

        self.setLayout(self.layout)

        self.setStyleSheet("""
            QWidget {
                background: rgba(10, 10, 10, 180);
                color: #d4c8a8;
                border: 1px solid #7a1f1f;
                border-radius: 10px;
                padding: 6px;
            }

            QLabel {
                font-size: 13px;
                border: none;
            }

            QLabel#panelTitle {
                color: #ff4444;
                font-size: 15px;
                font-weight: bold;
            }
        """)

    def add_line(self, text: str, icon: str | None = None):
        row_widget = QWidget()
        row_layout = QHBoxLayout()
        row_layout.setContentsMargins(0, 0, 0, 0)

        icon_label = QLabel()

        if icon:
            icon_label.setPixmap(get_pixmap(icon, 18))

        text_label = QLabel(text)

        row_layout.addWidget(icon_label)
        row_layout.addWidget(text_label)
        row_layout.addStretch()

        row_widget.setLayout(row_layout)

        self.layout.addWidget(row_widget)

        return {
            "row": row_widget,
            "icon": icon_label,
            "text": text_label
        }

    def set_line(self, line, text: str, icon: str | None = None, glow: bool = False):
        line["text"].setText(text)

        if icon:
            line["icon"].setPixmap(get_pixmap(icon, 18))

        if glow:
            line["text"].setStyleSheet("color: #8ea1ff; font-weight: bold;")
        else:
            line["text"].setStyleSheet("color: #d4c8a8; font-weight: normal;")