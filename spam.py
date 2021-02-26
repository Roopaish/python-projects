import pyautogui,time
time.sleep(5)
f = open("spams",'r',encoding="utf-8")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')