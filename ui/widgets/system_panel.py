from ui.widgets.base_panel import BasePanel
from modules.alliance.alliance_b_system.metrics import get_metrics


class SystemPanel(BasePanel):
    def __init__(self):
        super().__init__("ALLIANCE B / SYSTEM", "system")

        self.rows = [
            self.add_line("-", "cpu"),
            self.add_line("-", "gpu"),
            self.add_line("-", "temperature"),
            self.add_line("-", "ram"),
            self.add_line("-", "vram"),
            self.add_line("-", "disk"),
            self.add_line("-", "network"),
            self.add_line("-", "network")
        ]

    def refresh(self):
        data = get_metrics()

        values = [
            ("cpu", f"CPU: {data['cpu']}%"),
            ("gpu", f"GPU: {data['gpu']['usage_percent']}%"),
            ("temperature", f"GPU TEMP: {data['gpu']['temperature']}°C"),
            ("ram", f"RAM: {data['ram']['used_gb']}/{data['ram']['total_gb']} GB"),
            ("vram", f"VRAM: {data['gpu']['vram_used_mb']}/{data['gpu']['vram_total_mb']} MB"),
            ("disk", f"DISK FREE: {data['disk']['free_gb']} GB"),
            ("network", f"NET ↓ {data['network']['recv_mb']} MB"),
            ("network", f"NET ↑ {data['network']['sent_mb']} MB")
        ]

        for line, (icon, text) in zip(self.rows, values):
            self.set_line(line, text, icon)