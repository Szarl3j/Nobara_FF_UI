import psutil

class AllianceManager:
    def get_system_stats(self):
        """Lista C: Hardware jako członkowie party"""
        return [
            {"name": "CPU_CORE", "hp": psutil.cpu_percent(), "status": "online"},
            {"name": "RAM_MEM", "hp": psutil.virtual_memory().percent, "status": "online"},
            {"name": "GPU_CORE", "hp": 45, "status": "online"}, # Można rozbudować o pynvml
            # ... do 8 slotów
        ]

    def get_music_info(self):
        """Lista B: Orchestrion"""
        # Tu docelowo integracja z playerctl
        return {"title": "Answers", "artist": "Susan Calloway", "progress": 40}

    def get_discord_data(self):
        """Lista A: Social"""
        # Tu docelowo pypresence
        return [{"name": "Friend1", "status": "dnd"}, {"name": "Friend2", "status": "online"}]