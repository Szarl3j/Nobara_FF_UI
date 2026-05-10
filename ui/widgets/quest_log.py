from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QCheckBox,
    QHBoxLayout,
    QScrollArea
)

from core.paths import QUEST_LOG_CONFIG_FILE
from core.state import load_json, save_json
from core.icons import get_pixmap


class QuestLogWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.data = load_json(
            QUEST_LOG_CONFIG_FILE,
            {"categories": []}
        )

        self.main_layout = QVBoxLayout()

        self.title = QLabel("QUEST LOG")

        self.title.setStyleSheet("""
            color: #ffd700;
            font-size: 18px;
            font-weight: bold;
        """)

        self.main_layout.addWidget(self.title)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.content = QWidget()
        self.content_layout = QVBoxLayout()

        self.content.setLayout(self.content_layout)

        self.scroll.setWidget(self.content)

        self.main_layout.addWidget(self.scroll)

        self.setLayout(self.main_layout)

        self.setStyleSheet("""
            QWidget {
                background: rgba(5, 5, 8, 220);
                color: #d4c8a8;
                border: 1px solid #7a1f1f;
                border-radius: 10px;
            }

            QLabel {
                border: none;
            }

            QCheckBox {
                font-size: 13px;
                padding: 2px;
            }

            QScrollArea {
                border: none;
            }
        """)

        self.render()

    def render(self):
        while self.content_layout.count():
            child = self.content_layout.takeAt(0)

            if child.widget():
                child.widget().deleteLater()

        categories = self.data.get("categories", [])

        for category in categories:
            category_row = QHBoxLayout()

            icon_label = QLabel()

            icon_name = category.get(
                "icon",
                "TankRole.png"
            )

            icon_label.setPixmap(
                get_pixmap(icon_name, 22)
            )

            category_label = QLabel(
                category.get("name", "Category")
            )

            category_label.setStyleSheet("""
                color: #f5d98f;
                font-size: 15px;
                font-weight: bold;
            """)

            category_row.addWidget(icon_label)
            category_row.addWidget(category_label)
            category_row.addStretch()

            self.content_layout.addLayout(category_row)

            tasks = category.get("tasks", [])

            for task in tasks:
                task_row = QHBoxLayout()

                done = task.get("done", False)

                if done:
                    done_icon = QLabel()
                    done_icon.setPixmap(
                        get_pixmap("done.png", 16)
                    )

                    task_row.addWidget(done_icon)

                checkbox = QCheckBox(
                    task.get("text", "")
                )

                checkbox.setChecked(done)

                if done:
                    checkbox.setStyleSheet("""
                        color: #7fdc7f;
                        text-decoration: line-through;
                    """)

                checkbox.stateChanged.connect(
                    self.save_state
                )

                task_row.addWidget(checkbox)
                task_row.addStretch()

                self.content_layout.addLayout(task_row)

        self.content_layout.addStretch()

    def save_state(self):
        categories = self.data.get("categories", [])

        checkbox_widgets = []

        for i in range(self.content_layout.count()):
            item = self.content_layout.itemAt(i)

            if item.layout():
                layout = item.layout()

                for j in range(layout.count()):
                    widget_item = layout.itemAt(j)

                    if widget_item and widget_item.widget():
                        widget = widget_item.widget()

                        if isinstance(widget, QCheckBox):
                            checkbox_widgets.append(widget)

        checkbox_index = 0

        for category in categories:
            for task in category.get("tasks", []):
                if checkbox_index < len(checkbox_widgets):
                    checkbox = checkbox_widgets[checkbox_index]

                    task["done"] = checkbox.isChecked()

                checkbox_index += 1

        save_json(
            QUEST_LOG_CONFIG_FILE,
            self.data
        )

        self.render()

    def refresh(self):
        pass