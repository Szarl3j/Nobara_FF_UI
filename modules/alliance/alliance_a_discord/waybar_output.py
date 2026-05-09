from modules.alliance.alliance_a_discord.activity_store import get_activity


def main():
    data = get_activity()
    activity = data.get("activity", [])[:8]

    output = []

    for item in activity:
        name = item.get("name", "Unknown")
        glow = item.get("glow", False)

        output.append(f"✦ {name}" if glow else name)

    while len(output) < 8:
        output.append("-")

    print("A: " + " | ".join(output))


if __name__ == "__main__":
    main()