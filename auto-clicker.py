import pyautogui
import time
import sys

def evita_standby(inactivity_time):
    while True:
        
        pyautogui.press('capslock')
        print("Key pressed to avoid standby")
        time.sleep(inactivity_time)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <tempo_inattività_secondi>")
        sys.exit(1)

    try:
        inactivity_time = int(sys.argv[1])
    except ValueError:
        print("The idle time must be an integer number of seconds.")
        sys.exit(1)

    evita_standby(inactivity_time)
