import psutil
import datetime


class AllianceManager:
    def __init__(self):
        self.start_time = datetime.datetime.now()

    def get_hardware_stats(self):
        """Alliance C: Twoje podzespoły jako drużyna rajdowa"""
        # Pobieramy dane systemowe
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        net = psutil.net_io_counters()

        # Tworzymy listę 'członków party'
        party_c = [
            {"name": "CPU_CORE", "hp": cpu, "status": "online", "job": "DRG"},
            {"name": "RAM_MEM", "hp": ram, "status": "online", "job": "AST"},
            {"name": "DISK_ROOT", "hp": disk, "status": "online", "job": "WAR"},
            {"name": "NET_DOWN", "hp": min(100, net.bytes_recv // 1000000), "status": "online", "job": "BRD"},
        ]

        # Wypełniamy resztę do 8, żeby UI się nie rozjechało
        while len(party_c) < 8:
            party_c.append({"name": "Empty Slot", "hp": 0, "status": "offline", "job": "N/A"})

        return party_c

    def get_eorzea_time(self):
        """Symulacja czasu Eorzei (ET) - uproszczona"""
        now = datetime.datetime.now()
        # W FFXIV czas płynie ok. 20.5x szybciej. Tu robimy prosty zegar ET.
        return now.strftime("%H:%M")