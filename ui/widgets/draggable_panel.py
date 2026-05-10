from PySide6.QtWidgets import QFrame, QVBoxLayout, QSizeGrip
from PySide6.QtCore import Qt, QPoint


class DraggablePanel(QFrame):
    def __init__(self, child_widget, panel_id: str):
        super().__init__()

        self.child_widget = child_widget
        self.panel_id = panel_id

        self.dragging = False
        self.drag_position = QPoint()
        self.on_layout_changed = None

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMinimumSize(220, 160)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.child_widget)

        self.size_grip = QSizeGrip(self)
        self.layout.addWidget(
            self.size_grip,
            alignment=Qt.AlignBottom | Qt.AlignRight
        )

        self.setLayout(self.layout)

        self.setStyleSheet("""
            QFrame {
                background: rgba(10, 10, 10, 165);
                border: 1px solid #7a1f1f;
                border-radius: 12px;
            }
        """)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_position = (
                event.globalPosition().toPoint()
                - self.frameGeometry().topLeft()
            )
            event.accept()

    def mouseMoveEvent(self, event):
        if self.dragging and event.buttons() == Qt.LeftButton:
            self.move(
                event.globalPosition().toPoint()
                - self.drag_position
            )
            event.accept()

    def mouseReleaseEvent(self, event):
        self.dragging = False

        if self.on_layout_changed:
            self.on_layout_changed()

        event.accept()

    def resizeEvent(self, event):
        super().resizeEvent(event)

        if self.on_layout_changed:
            self.on_layout_changed()

    def refresh(self):
        if hasattr(self.child_widget, "refresh"):
            self.child_widget.refresh()