from modules.alliance.alliance_c_apps.running_apps import get_running_apps


def main():
    apps = get_running_apps()
    print("C: " + " | ".join(apps[:8]))


if __name__ == "__main__":
    main()