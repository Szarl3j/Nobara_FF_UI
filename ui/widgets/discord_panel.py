from ui.widgets.base_panel import BasePanel
from modules.alliance.alliance_a_discord.activity_store import get_activity


class DiscordPanel(BasePanel):
    def __init__(self):
        super().__init__("ALLIANCE A / DISCORD", "discord")

        self.rows = []

        for _ in range(8):
            self.rows.append(self.add_line("-", "message"))

    def refresh(self):
        data = get_activity()
        activity = data.get("activity", [])[:8]

        output = []

        for item in activity:
            output.append({
                "name": item.get("name", "Unknown"),
                "glow": item.get("glow", False)
            })

        while len(output) < 8:
            output.append({
                "name": "-",
                "glow": False
            })

        for line, item in zip(self.rows, output):
            self.set_line(
                line,
                item["name"],
                "notification" if item["glow"] else "message",
                item["glow"]
            )