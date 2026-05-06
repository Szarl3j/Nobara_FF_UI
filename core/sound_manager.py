import subprocess


def play(sound):
    subprocess.Popen([
        "play-sound",
        sound
    ])