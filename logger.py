from datetime import datetime
import os

LOG = "Logs/kitchen.log"

os.makedirs("Logs", exist_ok=True)

def log(message):

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = f"[{now}] {message}"

    print(line)

    with open(LOG, "a", encoding="utf8") as f:
        f.write(line + "\n")