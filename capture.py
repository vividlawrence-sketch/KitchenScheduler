import subprocess
import os

ADB = r"C:\Program Files\BlueStacks_nxt\HD-Adb.exe"

OUTPUT = "Images/current.png"


def capture():

    os.makedirs("Images", exist_ok=True)

    with open(OUTPUT, "wb") as f:

        subprocess.run(
            [
                ADB,
                "exec-out",
                "screencap",
                "-p"
            ],
            stdout=f
        )

    return OUTPUT