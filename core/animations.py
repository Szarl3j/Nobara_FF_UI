from PySide6.QtCore import QVariantAnimation, QEasingCurve

def animate_bar(progress_bar, start_val, end_val, duration=400):
    """Płynnie przesuwa pasek postępu."""
    anim = QVariantAnimation(progress_bar)
    anim.setStartValue(start_val)
    anim.setEndValue(end_val)
    anim.setDuration(duration)
    anim.setEasingCurve(QEasingCurve.OutQuad)
    anim.valueChanged.connect(progress_bar.setValue)
    anim.start()
    # Ważne: trzeba zachować referencję, żeby GC nie usunął animacji
    progress_bar._current_anim = anim