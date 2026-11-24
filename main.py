"""One-line roast of a fitness gadget.

The joke: a smartwatch treats the tiniest movement (standing up to
grab food from the fridge) like a heroic Everest climb, mocking how
eagerly wearables hand out praise for doing almost nothing.
"""
import os

LINE = "My smartwatch congratulates me for standing up, like I just climbed Everest instead of reaching for the fridge."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
