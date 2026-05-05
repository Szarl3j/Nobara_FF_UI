from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QProgressBar
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve


class LimitBreakWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Etykieta LIMIT BREAK
        self.label = QLabel("LIMIT BREAK")
        self.label.setStyleSheet("color: #ffaa00; font-family: 'Cinzel'; font-size: 10px; font-weight: bold;")
        layout.addWidget(self.label)

        self.bar_layout = QHBoxLayout()
        self.bars = []

        for _ in range(3):
            bar = QProgressBar()
            bar.setFixedSize(60, 12)
            bar.setTextVisible(False)
            bar.setRange(0, 100)
            bar.setStyleSheet(self._get_bar_style("#444"))  # Domyślnie pusty
            self.bar_layout.addWidget(bar)
            self.bars.append(bar)

        layout.addLayout(self.bar_layout)

    def _get_bar_style(self, color):
        return f"""
            QProgressBar {{ background: rgba(20,20,20,0.8); border: 1px solid #c2a661; border-radius: 2px; }}
            QProgressBar::chunk {{ background: {color}; }}
        """

    def update_lb(self, system_load):
        # system_load to wartość 0-100 (np. średnie obciążenie CPU)
        for i, bar in enumerate(self.bars):
            threshold = (i + 1) * 33
            if system_load >= threshold:
                bar.setValue(100)
                color = "#ffcc00" if i < 2 else "#ff3300"  # LB3 jest czerwonawe
                bar.setStyleSheet(self._get_bar_style(color))
            else:
                bar.setValue(0)
                bar.setStyleSheet(self._get_bar_style("#444"))