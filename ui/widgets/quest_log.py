from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class QuestLogWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.title = QLabel("TO DO")
        self.q1 = QLabel("Discord listener active")
        self.q2 = QLabel("System monitor active")
        self.q3 = QLabel("Apps monitor active")
        self.q4 = QLabel("Skillbar ready")

        layout.addWidget(self.title)
        layout.addWidget(self.q1)
        layout.addWidget(self.q2)
        layout.addWidget(self.q3)
        layout.addWidget(self.q4)

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
                font-size: 13px;
            }

            QLabel:first-child {
                color: #ff4444;
                font-weight: bold;
            }
        """)

    def refresh(self):
        pass