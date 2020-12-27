import pyautogui
im = pyautogui.screenshot(region=(pyautogui.position()[0],pyautogui.position()[1],pyautogui.position()[0],pyautogui.position()[1]))
c=im.getpixel((0,0))
while pyautogui.onScreen(pyautogui.position()):
    if(c[1]>c[0] and c[1]>c[2]):
        pyautogui.click()
    im = pyautogui.screenshot(region=(pyautogui.position()[0],pyautogui.position()[1],pyautogui.position()[0],pyautogui.position()[1]))
    c=im.getpixel((0,0))
