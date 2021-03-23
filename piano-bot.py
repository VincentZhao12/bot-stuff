from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x, y):
    # print("Clicking at x: " + x + ", y: " + y)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Left: (825, 700)
# Left Center: (725, 700)
# Right Center: (625, 700)
# Left Center: (525, 700)

left = 825
leftCenter = 725
rightCenter = 625
right = 525

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(left, 700)[0] == 0:
        click(left, 700)
    if pyautogui.pixel(leftCenter, 700)[0] == 0:
        click(leftCenter, 700)
    if pyautogui.pixel(rightCenter, 700)[0] == 0:
        click(rightCenter, 700)
    if pyautogui.pixel(right, 700)[0] == 0:
        click(right, 700)