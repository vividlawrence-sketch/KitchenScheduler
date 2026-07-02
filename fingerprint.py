import hashlib
import re

def normalize(text: str) -> str:
    if text is None:
        return ""

    text = text.upper()

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove queue timer (changes every second)
    text = re.sub(r"\d{2}:\d{2}:\d{2}", "", text)

    return text.strip()


def create_fingerprint(parsed):

    pieces = []

    # Printed time (stable)
    pieces.append(normalize(parsed.get("printed_time")))

    # Slot time (6PM etc.)
    pieces.append(normalize(parsed.get("slot_time")))

    # Pizza list
    for item in sorted(parsed["items"], key=lambda x: x["pizza"]):
        pieces.append(
            f'{item["qty"]}-{item["source"]}-{item["pizza"]}'
        )

    raw = "|".join(pieces)

    return hashlib.sha256(raw.encode()).hexdigest()