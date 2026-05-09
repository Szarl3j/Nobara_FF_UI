import platform
import shutil
import subprocess

import psutil

from core.paths import SYSTEM_STATUS_FILE
from core.state import save_json


IS_WINDOWS = platform.system() == "Windows"


def get_cpu():
    try:
        return round(psutil.cpu_percent(interval=0.2), 1)

    except Exception:
        return 0.0


def get_ram():
    try:
        ram = psutil.virtual_memory()

        return {
            "percent": round(ram.percent, 1),
            "used_gb": round(ram.used / 1024 / 1024 / 1024, 1),
            "total_gb": round(ram.total / 1024 / 1024 / 1024, 1)
        }

    except Exception:
        return {
            "percent": 0,
            "used_gb": 0,
            "total_gb": 0
        }


def get_swap():
    try:
        swap = psutil.swap_memory()

        return {
            "percent": round(swap.percent, 1)
        }

    except Exception:
        return {
            "percent": 0
        }


def get_disk():
    try:
        disk = psutil.disk_usage("/")

        return {
            "percent": round(disk.percent, 1),
            "free_gb": round(disk.free / 1024 / 1024 / 1024, 1)
        }

    except Exception:
        return {
            "percent": 0,
            "free_gb": 0
        }


def get_network():
    try:
        net = psutil.net_io_counters()

        return {
            "sent_mb": round(net.bytes_sent / 1024 / 1024, 1),
            "recv_mb": round(net.bytes_recv / 1024 / 1024, 1)
        }

    except Exception:
        return {
            "sent_mb": 0,
            "recv_mb": 0
        }


def get_gpu():
    """
    Windows/Linux safe.
    """
    try:
        nvidia_smi = shutil.which("nvidia-smi")

        if not nvidia_smi:
            return {
                "usage_percent": 0,
                "vram_used_mb": 0,
                "vram_total_mb": 0,
                "temperature": 0
            }

        result = subprocess.check_output(
            [
                nvidia_smi,
                "--query-gpu=utilization.gpu,memory.used,memory.total,temperature.gpu",
                "--format=csv,noheader,nounits"
            ],
            text=True
        ).strip()

        gpu, used, total, temp = [
            x.strip()
            for x in result.split(",")
        ]

        return {
            "usage_percent": int(gpu),
            "vram_used_mb": int(used),
            "vram_total_mb": int(total),
            "temperature": int(temp)
        }

    except Exception:
        return {
            "usage_percent": 0,
            "vram_used_mb": 0,
            "vram_total_mb": 0,
            "temperature": 0
        }


def get_load():
    """
    Linux only.
    """
    try:
        if IS_WINDOWS:
            return 0.0

        return round(psutil.getloadavg()[0], 2)

    except Exception:
        return 0.0


def collect_system_status():
    data = {
        "cpu": get_cpu(),
        "ram": get_ram(),
        "swap": get_swap(),
        "disk": get_disk(),
        "network": get_network(),
        "gpu": get_gpu(),
        "load": get_load(),
        "platform": platform.system()
    }

    save_json(SYSTEM_STATUS_FILE, data)

    return data


if __name__ == "__main__":
    import json

    data = collect_system_status()

    print(json.dumps(data, indent=2))