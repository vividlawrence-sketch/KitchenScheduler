import cv2
import os
from layout import *

def detect_cards(image_path):

    image = cv2.imread(image_path)

    h, w = image.shape[:2]

    os.makedirs("Images/Cards", exist_ok=True)
    os.makedirs("Images/Debug", exist_ok=True)

    debug = image.copy()

    cards = []

    card = 0

    x = FIRST_CARD_X

    while x + CARD_WIDTH <= w:

        roi = image[
            FIRST_CARD_Y:FIRST_CARD_Y + CARD_HEIGHT,
            x:x + CARD_WIDTH
        ]

        if roi.size == 0:
            break

        filename = f"Images/Cards/card_{card}.png"

        cv2.imwrite(filename, roi)

        cards.append(filename)

        cv2.rectangle(
            debug,
            (x, FIRST_CARD_Y),
            (x + CARD_WIDTH, FIRST_CARD_Y + CARD_HEIGHT),
            (0,255,0),
            3
        )

        card += 1

        x += CARD_WIDTH + CARD_GAP

    cv2.imwrite(
        "Images/Debug/debug_detection.png",
        debug
    )

    print("Cards Saved:", len(cards))

    return cards