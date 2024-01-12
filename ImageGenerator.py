import pyautogui
import time
import random
keyset1=["i","h","t","c","v","n"]
keysetI=["a","e","b","c","i","f","g","l","p","o","r","n","t","x","u","v","m","w"]
keysetH=["a","b","d","e","u","l","g","h","m","v","p","s","t","u","n","o"]
keysetT=["b","e","c","g","i","t","m","u","n","p","s","v","w","h"]
keysetC=["b","g","h","l","r","i","m"]
keysetV=["b","d","m","n","o","v","e","r","t"]
keysetN=["b","c","r","o","x","f","m","a","i","t","h","e","s","v","w"]
the=100
pyautogui.hotkey("alt","tab")
for x in range(7):
    yy= random.randint(0,5)
    yyy= random.randint(0,17)
    zz= random.randint(0,13)
    zzz= random.randint(0,15)
    zy= random.randint(0,6)
    zzy= random.randint(0,8)
    zzyy=random.randint(0,14)
    time.sleep(2)
    pyautogui.moveTo(300,75)
    pyautogui.click()
    pyautogui.press(keyset1[yy])
    if yy==0 and x==0:
        pyautogui.press(keysetI[yyy])
    elif yy==1:
        pyautogui.press(keysetH[zzz])
    elif yy==2:
        pyautogui.press(keysetT[zz])
    elif yy==3:
        pyautogui.press(keysetC[zy])
    elif yy==4:
        pyautogui.press(keysetV[zzy])
    elif yy==5:
        pyautogui.press(keysetN[zzyy])  
    pyautogui.moveTo(the,500)   
    pyautogui.click()
    the+=150
pyautogui.moveTo(300,75)
pyautogui.click()
pyautogui.press("o")
pyautogui.press("m")
pyautogui.moveTo(the,500)
pyautogui.click()
the=100
pyautogui.moveTo(100,400)
pyautogui.keyDown("alt")
the+=160
pyautogui.dragTo(the,400,.75,button="right")
the+=160
pyautogui.dragTo(the,400,.75,button="right")
the+=160
pyautogui.dragTo(the,400,.75,button="right")
the+=160
pyautogui.dragTo(the,400,.75,button="right")
the+=160
pyautogui.dragTo(the,400,.75,button="right")
the+=160
pyautogui.dragTo(the,400,.75,button="right")
the+=160
pyautogui.dragTo(the,400,.75,button="right")
the+=160
pyautogui.keyUp("alt")
pyautogui.moveTo(35,75)
pyautogui.click()
pyautogui.press("d")
pyautogui.moveTo(1520,75)
pyautogui.click()
pyautogui.moveTo(35,75)
time.sleep(1)
pyautogui.keyDown('Win')
pyautogui.keyDown('shift')
pyautogui.keyDown('s')
pyautogui.moveTo(625,375)
pyautogui.hold()
pyautogui.dragTo(900,700)
pyautogui.keyUp('shift')
pyautogui.keyUp('s')
pyautogui.keyUp('win')
pyautogui.click()