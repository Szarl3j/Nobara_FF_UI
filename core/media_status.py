import subprocess


def now_playing():
    try:
        title = subprocess.check_output(
            ["playerctl", "metadata", "title"],
            text=True
        ).strip()

        return title

    except Exception:
        return "No Media"