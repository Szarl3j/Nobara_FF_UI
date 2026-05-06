import subprocess

try:
    title = subprocess.check_output(
        ["playerctl", "metadata", "title"],
        text=True
    ).strip()

    artist = subprocess.check_output(
        ["playerctl", "metadata", "artist"],
        text=True
    ).strip()

    print(f"{artist} - {title}")

except Exception:
    print("No Media")