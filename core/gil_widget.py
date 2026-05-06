class GilWidget:

    def __init__(self):
        self.value = 0

    def update_value(self, value):
        self.value = int(
            str(value)
            .replace(" ", "")
            .replace(",", "")
        )

    def formatted(self):
        return f"{self.value:,}"