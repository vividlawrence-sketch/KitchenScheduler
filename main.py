from capture import capture
from detect_cards import detect_cards
from ocr import read_card
from parser import parse_card

print("Kitchen Scheduler")

image = capture()

cards = detect_cards(image)

print(f"Detected {len(cards)} cards")

for i, card in enumerate(cards):

    print("=" * 60)

    text = read_card(card)

    parsed = parse_card(text)

    print(text)

    print()

    print(parsed)