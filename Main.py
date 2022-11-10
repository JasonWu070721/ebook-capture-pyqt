import keyboard
import time
import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui

def copy_all_page():
    process_count = 0
    while process_count < 400:

        keyboard.press_and_release('f5')
        print("f5")
        time.sleep(1)

        keyboard.press_and_release('right')
        print("right")

        time.sleep(2)
        process_count = process_count + 1

if __name__ == '__main__':

    while True:
        if keyboard.read_key() == "p":
            print("Screen capture stoping.")
            
            copy_all_page()
            break

