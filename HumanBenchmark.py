import pyautogui, time
pyautogui.click(x=200, y=200)
for i in range(5):
    c=(43, 135, 209)
    while(c[1]<=c[0] or c[1]<=c[2]):
        im2 = pyautogui.screenshot(region=(200,200,200,200))
        c=im2.getpixel((0,0))
    pyautogui.click(x=200, y=200)
    print(i+1)
    time.sleep(1)
    pyautogui.click(x=200, y=200)
print("done")
