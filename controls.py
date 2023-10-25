import pyautogui
import win32api
import win32con
import time
import numpy as np
from datetime import datetime

#Função Clicar
def clicar(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(np.random.uniform(2,3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Achar posição imagem
def Posicao_Imagem(img):
    return pyautogui.locateCenterOnScreen('./resources/' + img + '.png',confidence=0.8)

#Clicar imagem
def Clicar_Imagem(imgName):
    pos = Posicao_Imagem(imgName)
    if pos is not None:
        clicar(pos.x,pos.y)
        pyautogui.moveTo(np.random.uniform(0,100), np.random.uniform(0,100))
        time.sleep(np.random.uniform(2,3))

#Achar a imagem na tela
def Achar_Imagem_Tela(img):
    return pyautogui.locateOnScreen('./resources/' + img + '.png', confidence=0.9) != None

#Timestamp no print
old_print = print

def timestamped_print(*args, **kwargs):
  old_print(datetime.now(), ':' , *args, **kwargs)

print = timestamped_print