import random
from PySide6.QtWidgets import QWidget, QHBoxLayout, QFrame
from PySide6.QtCore import QTimer


class AudioVisualizer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 20)
        layout = QHBoxLayout(self)
        layout.setSpacing(2)
        layout.setContentsMargins(0, 0, 0, 0)

        self.bars = []
        for _ in range(10):
            f = QFrame()
            f.setFixedWidth(4)
            f.setStyleSheet("background: #3fb361; border-radius: 1px;")
            layout.addWidget(f)
            self.bars.append(f)

    def animate(self, active=True):
        for b in self.bars:
            h = random.randint(2, 18) if active else 2
            b.setFixedHeight(h)