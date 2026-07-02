import re

PIZZAS = [
    "CLASSIC CHEESE",
    "HAWAIIAN",
    "PEPPERONI",
    "MARGHERITA",
    "PEPPER BEEF",
    "BACON CHEESE",
    "THREE CHEESE",
    "VEGIZZA",
    "ALL MEAT",
    "HAMZARELLA",
    "MANHATTAN",
    "PESTO",
    "KANIYAKI",
    "GARLIC SEAFOOD"
]


def parse_card(text):

    result = {
        "queue_number": None,
        "queue_timer": None,
        "printed_time": None,
        "slot_time": None,
        "items": []
    }

    # Queue Number
    m = re.search(r"Order#[:\s]*(\d+)", text, re.IGNORECASE)
    if m:
        result["queue_number"] = m.group(1)

    # Queue Timer (HH:MM:SS)
    m = re.search(r"\b\d{2}:\d{2}:\d{2}\b", text)
    if m:
        result["queue_timer"] = m.group(0)

    # Printed Time (e.g. 3:18PM or 3:18 PM)
    times = re.findall(r"\b\d{1,2}:\d{2}\s?(?:AM|PM|am|pm)\b", text)
    if times:
        result["printed_time"] = times[-1]

    # Slot Time (e.g. 6PM, 6:00 PM)
    slot = re.search(r"\b(\d{1,2})(?::(\d{2}))?\s?(AM|PM|am|pm)\b", text)
    if slot:
        result["slot_time"] = slot.group(0)

    lines = text.upper().splitlines()

    for line in lines:

        qty = 1

        q = re.search(r"(\d+)X", line)

        if q:
            qty = int(q.group(1))

        source = "Walk-in"

        if "DEL" in line:
            source = "DEL"

        elif "FP" in line:
            source = "FP"

        elif "GF" in line:
            source = "GF"

        elif "TO" in line:
            source = "TO"

        for pizza in PIZZAS:

            if pizza in line:

                result["items"].append({

                    "qty": qty,
                    "source": source,
                    "pizza": pizza

                })

    return result