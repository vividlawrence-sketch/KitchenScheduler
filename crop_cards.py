from PIL import Image
import os

CARD_WIDTH = 520
CARD_HEIGHT = 760

FIRST_CARD_X = 145
FIRST_CARD_Y = 175

CARD_GAP = 35

VISIBLE_CARDS = 4


def crop_cards(image_path):

    os.makedirs("Images/Cards", exist_ok=True)

    image = Image.open(image_path)

    saved = []

    for i in range(VISIBLE_CARDS):

        x = FIRST_CARD_X + i * (CARD_WIDTH + CARD_GAP)
        y = FIRST_CARD_Y

        crop = image.crop(
            (
                x,
                y,
                x + CARD_WIDTH,
                y + CARD_HEIGHT
            )
        )

        filename = f"Images/Cards/card_{i+1}.png"

        crop.save(filename)

        saved.append(filename)

    return saved