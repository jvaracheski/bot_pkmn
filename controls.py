import pyautogui
import win32api
import win32con
import time
import numpy as np
import os
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


def checar_captcha():
    if Achar_Imagem_Tela('captcha'):
        print('Achei captcha!')
        return True
    else:
        print('Não achei captcha!')
        return False
    
def linkar_nomes():
    dir_path = r'./resources/nomes/'
    res = []
    for file_path in os.listdir(dir_path):
    # check if current file_path is a file
        if os.path.isfile(os.path.join(dir_path, file_path)):
            # add filename to list
            res.append(file_path.replace('.png',''))
    return res

def resolver_captcha():
    time.sleep(np.random.uniform(2,3))
    #clicar na box
    Clicar_Imagem('click_captcha')
    time.sleep(5)
    lista_nomes = linkar_nomes()
    var = 0
    while Achar_Imagem_Tela ('captcha_check'):
        for nome in lista_nomes:
        #validar qual pokemon
            if Achar_Imagem_Tela('nomes/' + nome):
                Clicar_Imagem('pokemon/' + nome)
                print('Resolvido o captcha, bobão!')
        var += 1
        if var >= 5:
            pyautogui.keyDown('f5')
            time.sleep(0.1)
            pyautogui.keyUp('f5')