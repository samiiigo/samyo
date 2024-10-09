import pyautogui,time,random,sys

time.sleep(1)
x,y = 345,468
try:
    for i in range(50):
        pyautogui.click(random.randint(x-50,x+50),random.randint(y-50,y+50),clicks=20)
        pyautogui.click(random.randint(x-50,x+50),random.randint(y-50,y+50),clicks=20)

except KeyboardInterrupt:
    print ('\n')

    