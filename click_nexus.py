from datetime import datetime, timedelta
import os
from time import sleep

import pyautogui as gui

IMAGE_FILE = os.path.join("slow-download.png")
CONFIDENCE = 0.7
RANDOMIZE_PIXELS = 5  # Number of pixels to randomize in click
GRAYSCALE = False


def find_button(image):
    """
    Attempts to find the button by image.
    """
    start = datetime.now()

    print("Finding the button... ")
    location = None
    counter = 0

    while location is None:
        counter += 1
        print(counter, end="... ")
        location = gui.locateCenterOnScreen(
            image, confidence=CONFIDENCE, grayscale=GRAYSCALE
        )
        if datetime.now() > start + timedelta(seconds=2.5):
            print("Breaking, no button found!")
            return None

    print(f"Found button at location: {location}...")

    return location


def click_button(image):
    while True:
        location = None
        location = find_button(image)

        if location:
            gui.click(location)
            sleep(5)


if __name__ == "__main__":
    click_button(IMAGE_FILE)
