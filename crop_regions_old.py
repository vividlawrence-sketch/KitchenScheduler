import os
import cv2

OCR_FOLDER = "OCR"

os.makedirs(OCR_FOLDER, exist_ok=True)


def crop_regions(card_path, card_id):

    card = cv2.imread(card_path)

    h, w = card.shape[:2]

    # ---------- ORDER NUMBER ----------
    order = card[0:90, 0:250]

    # ---------- QUEUE TIMER ----------
    timer = card[0:90, w-180:w]

    # ---------- ITEMS ----------
    items = card[90:h-140, 0:w]

    # ---------- PRINT TIME ----------
    printed = card[h-120:h, 0:230]

    # ---------- NOTE AREA ----------
    note = card[90:190, 0:w]

    paths = {
        "order":f"OCR/{card_id}_order.png",
        "timer":f"OCR/{card_id}_timer.png",
        "items":f"OCR/{card_id}_items.png",
        "printed":f"OCR/{card_id}_printed.png",
        "note":f"OCR/{card_id}_note.png"
    }

    cv2.imwrite(paths["order"],order)
    cv2.imwrite(paths["timer"],timer)
    cv2.imwrite(paths["items"],items)
    cv2.imwrite(paths["printed"],printed)
    cv2.imwrite(paths["note"],note)

    return paths