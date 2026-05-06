import subprocess


def notify(title, message):
    subprocess.run([
        "notify-send",
        title,
        message
    ])