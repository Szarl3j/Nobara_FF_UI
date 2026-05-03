import psutil

class AllianceManager:
    def __init__(self):
        pass

    def _fill_to_eight(self, current_list):
        """Dopełnia listę do 8 członków, aby zachować strukturę raidu."""
        while len(current_list) < 8:
            current_list.append({
                "name": "Empty Slot",
                "hp": 0,
                "status": "offline",
                "job": "NONE"
            })
        return current_list[:8] # Upewnia się, że nie ma więcej niż 8

    def get_social_info(self):
        """GRUPA A: SOCIAL / PARTY (8 slotów)"""
        party = [
            {"name": "Ty (Warrior)", "hp": 100, "status": "online", "job": "WAR"},
            {"name": "Marek (Friend)", "hp": 100, "status": "online", "job": "BLM"},
            {"name": "Ania (Friend)", "hp": 100, "status": "online", "job": "WHM"},
        ]
        return self._fill_to_eight(party)

    def get_music_info(self):
        """GRUPA B: ORCHESTRION / AMBIENT (8 slotów)"""
        # Tutaj możemy potraktować muzykę jako lidera grupy B,
        # a resztę slotów jako 'efekty dźwiękowe' lub puste miejsca.
        orchestrion = [
            {"name": "Susan Calloway - Answers", "hp": 65, "status": "playing", "job": "BRD"},
            {"name": "System Sounds", "hp": 100, "status": "online", "job": "PLD"},
        ]
        return self._fill_to_eight(orchestrion)

    def get_system_stats(self):
        """GRUPA C: HARDWARE ALLIANCE (8 slotów)"""
        # Mapujemy Twoje podzespoły na konkretne Joby z gry
        hardware = [
            {"name": "CPU_CORE", "hp": psutil.cpu_percent(), "status": "online", "job": "DRK"},
            {"name": "RAM_MEM", "hp": psutil.virtual_memory().percent, "status": "online", "job": "ALC"},
            {"name": "GPU_CORE", "hp": 45, "status": "online", "job": "MCH"},
            {"name": "DISK_C", "hp": psutil.disk_usage('C:').percent, "status": "online", "job": "MIN"},
            {"name": "NETWORK", "hp": 12, "status": "online", "job": "NIN"},
            {"name": "FANS_SPEED", "hp": 30, "status": "online", "job": "VPR"},
        ]
        return self._fill_to_eight(hardware)