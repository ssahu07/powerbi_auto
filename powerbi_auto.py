import csv
import os
import time
import psutil as psutil
import pyautogui
from pywinauto.application import Application

print("1. Closing all background running PowerBI instances")
# Kill running PBI
PROCNAME = "PBIDesktop.exe"
for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == PROCNAME:
        proc.kill()

i = 0
# Opening Connection csv

f = open(r'C:\Users\ssahu\Desktop\PowerBI_auto\PowerBI_Input.csv')  # Update csv path and connection same as PowerBI_Input.csv
csv_f = csv.reader(f)

for row in csv_f:
    for col in csv_f:
        i += 1
        print("2. Opening Visualisation:", i)
        try:
            os.startfile(col[0])
        except Exception:
            print('File Not Found')

        app = Application(backend='uia').connect(path=PROCNAME)
        win = app.window(title_re='.*Power BI Desktop')
        time.sleep(15)
        win.set_focus()

        time.sleep(10)
        # print(pyautogui.position())
        pyautogui.hotkey('ctrl', 'f6')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'f6')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'f6')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'f6')
        time.sleep(1)
        pyautogui.hotkey('tab')
        time.sleep(1)
        pyautogui.hotkey('tab')
        time.sleep(1)
        pyautogui.hotkey('right')
        time.sleep(1)
        pyautogui.hotkey('right')
        time.sleep(.1)
        pyautogui.hotkey('right')
        time.sleep(.1)
        pyautogui.hotkey('right')
        time.sleep(.1)
        pyautogui.hotkey('right')
        time.sleep(.1)
        pyautogui.hotkey('right')
        time.sleep(.1)
        pyautogui.hotkey('right')
        time.sleep(.1)
        pyautogui.hotkey('right')
        time.sleep(.1)
        pyautogui.hotkey('right')
        time.sleep(.1)
        pyautogui.hotkey('right')
        time.sleep(.1)
        pyautogui.hotkey('right')
        time.sleep(.1)
        pyautogui.hotkey('enter')
        time.sleep(4)
        pyautogui.hotkey('alt', 'h')
        time.sleep(3)
        pyautogui.hotkey('q')
        time.sleep(1)
        pyautogui.press('tab', presses=2)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.hotkey('del')
        print("3. Deleted Old connection details in advanced Editor")
        temp = col[1]
        pyautogui.write(temp, interval=0.08)
        time.sleep(1)

        # Saving new connection string
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')

        # Refreshing Table
        pyautogui.hotkey('alt', 'h')
        pyautogui.hotkey('r')
        time.sleep(1)
        pyautogui.hotkey('enter')


        # Close and Apply
        pyautogui.hotkey('alt', 'h')
        pyautogui.hotkey('c')

        time.sleep(1)
        pyautogui.hotkey('enter')
        win.set_focus()
        print("5. Added new connection details and Applied Changes")

        # Refresh
        print("6. Refreshing")
        pyautogui.hotkey('right')
        pyautogui.hotkey('enter')