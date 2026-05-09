from modules.alliance.alliance_b_system.metrics import get_metrics


def main():
    data = get_metrics()

    cpu = data["cpu"]
    ram = data["ram"]
    gpu = data["gpu"]
    disk = data["disk"]
    network = data["network"]

    items = [
        f"CPU {cpu}%",
        f"GPU {gpu['usage_percent']}%",
        f"GT {gpu['temperature']}°C",
        f"RAM {ram['used_gb']}/{ram['total_gb']}GB",
        f"DISK {disk['free_gb']}GB",
        f"NET ↓{network['recv_mb']}MB",
        f"NET ↑{network['sent_mb']}MB",
        "SYS OK"
    ]

    print("B: " + " | ".join(items))


if __name__ == "__main__":
    main()