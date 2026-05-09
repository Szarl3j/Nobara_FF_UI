from core.system_monitor import collect_system_status


def get_metrics():
    return collect_system_status()