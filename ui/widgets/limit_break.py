import psutil

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QProgressBar
)

from PySide6.QtCore import Qt


class LimitBreakWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.title = QLabel("LIMIT BREAK")
        self.title.setAlignment(Qt.AlignCenter)

        # GPU
        self.gpu_label = QLabel("GPU")
        self.gpu_bar = QProgressBar()

        # CPU
        self.cpu_label = QLabel("CPU")
        self.cpu_bar = QProgressBar()

        # RAM
        self.ram_label = QLabel("RAM")
        self.ram_bar = QProgressBar()

        self.setup_bar(self.gpu_bar)
        self.setup_bar(self.cpu_bar)
        self.setup_bar(self.ram_bar)

        gpu_layout = self.create_section(
            self.gpu_label,
            self.gpu_bar
        )

        cpu_layout = self.create_section(
            self.cpu_label,
            self.cpu_bar
        )

        ram_layout = self.create_section(
            self.ram_label,
            self.ram_bar
        )

        bars_layout = QHBoxLayout()
        bars_layout.addLayout(gpu_layout)
        bars_layout.addLayout(cpu_layout)
        bars_layout.addLayout(ram_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title)
        main_layout.addLayout(bars_layout)

        main_layout.setContentsMargins(10, 6, 10, 6)
        main_layout.setSpacing(4)

        self.setLayout(main_layout)

        # STAŁY ROZMIAR
        self.setFixedWidth(360)
        self.setFixedHeight(90)

        self.setStyleSheet("""
            QWidget {
                background: rgba(5, 5, 8, 220);
                border: 1px solid #7a1f1f;
                border-radius: 0px;
            }

            QLabel {
                color: #d4c8a8;
                font-size: 12px;
                font-weight: bold;
                border: none;
            }

            QProgressBar {
                background: rgba(20, 20, 20, 220);
                border: 1px solid #5c1010;
                border-radius: 4px;

                text-align: center;

                color: white;

                min-height: 16px;
                max-height: 16px;
            }

            QProgressBar::chunk {
                background-color: #b00000;
                border-radius: 3px;
            }
        """)

    def create_section(self, label, bar):
        layout = QVBoxLayout()

        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(bar)
        layout.addWidget(label)

        layout.setSpacing(2)

        return layout

    def setup_bar(self, bar):
        bar.setMinimum(0)
        bar.setMaximum(100)
        bar.setValue(0)
        bar.setTextVisible(False)

    def refresh(self):
        # CPU
        cpu_usage = int(psutil.cpu_percent())
        self.cpu_bar.setValue(cpu_usage)

        # RAM
        ram_usage = int(psutil.virtual_memory().percent)
        self.ram_bar.setValue(ram_usage)

        # GPU
        # Placeholder dopóki nie dodamy pynvml
        gpu_usage = min(
            100,
            int((cpu_usage + ram_usage) / 2)
        )

        self.gpu_bar.setValue(gpu_usage)

        self.update_colors(
            self.cpu_bar,
            cpu_usage
        )

        self.update_colors(
            self.ram_bar,
            ram_usage
        )

        self.update_colors(
            self.gpu_bar,
            gpu_usage
        )

    def update_colors(self, bar, value):
        if value >= 92:
            color = "#ff2020"

        elif value >= 75:
            color = "#ff8800"

        else:
            color = "#b00000"

        bar.setStyleSheet(f"""
            QProgressBar {{
                background: rgba(20, 20, 20, 220);
                border: 1px solid #5c1010;
                border-radius: 4px;

                min-height: 16px;
                max-height: 16px;
            }}

            QProgressBar::chunk {{
                background-color: {color};
                border-radius: 3px;
            }}
        """)