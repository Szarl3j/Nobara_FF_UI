import psutil


def process_exists(name: str):
    for proc in psutil.process_iter(["name"]):
        try:
            proc_name = proc.info["name"]

            if proc_name and name.lower() in proc_name.lower():
                return True

        except Exception:
            pass

    return False


def list_processes():
    processes = []

    for proc in psutil.process_iter(["name"]):
        try:
            name = proc.info["name"]

            if name:
                processes.append(name)

        except Exception:
            pass

    return sorted(list(set(processes)))