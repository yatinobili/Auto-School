import pyautogui
import time
import keyboard
import random
import win32api, win32con
import webbrowser

url = 'https://meet.google.com/cnu-mfbq-wag'

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


webbrowser.open(url)
time.sleep(8)

if pyautogui.locateOnScreen('mute.png', confidence = 0.7) !=None:
    click(1007, 580)
    time.sleep(1)

if pyautogui.locateOnScreen('cam.png', confidence = 0.7) !=None:
    click(1090, 580)
    time.sleep(1)

if pyautogui.locateOnScreen('join.png', confidence = 0.7) !=None:
    click(1583, 417)
    time.sleep(1)

