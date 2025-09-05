import pyautogui
import time
from datetime import datetime, timedelta

def mover_mouse_durante_una_hora(interval_sendouts=3):
    fin = datetime.now() + timedelta(hours=2)
    print(f"Starting movement del mouse cada {interval_sendouts} seconds...")

    while datetime.now() < fin:
        # Get the current position of the mouse
        x, y = pyautogui.position()
        # Mouse movement to a new position
        pyautogui.moveTo(x + 100, y + 100, duration=0.2)
        pyautogui.moveTo(x, y, duration=0.2)
        print(f"Movement performed at {datetime.now().strftime('%H:%M:%S')}")
        time.sleep(interval_sendouts)

    print("Movements completed.")

if __name__ == "__main__":
    mover_mouse_durante_una_hora()
