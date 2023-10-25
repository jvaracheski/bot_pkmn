from pyautogui import *
import pyautogui
import time
import numpy as np
import keyboard
import win32api
import win32con

# Esperar um pouco
time.sleep(5)

#Preparando para clicar
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

acabouPP = False
pp_total = 15
contador_pp = 0
x = False

#Colocando botão para ligar/parar
while keyboard.is_pressed('q') is False:
    while not Achar_Imagem_Tela('captcha'):
        if x is False:
            print('Preparando para Iniciar')
            if Achar_Imagem_Tela('poke_center'):
                time.sleep(2)
                Clicar_Imagem('poke_center')
                print('Entrando Poke Center')
                time.sleep(2)
                Clicar_Imagem('heal')
                print('Curando ~~')
                time.sleep(2)
                if Achar_Imagem_Tela('heal_success'):
                    acabouPP = False
                    contador_pp = 0
                    x = True
                    print('Pokemons curados com sucesso!')
                    time.sleep(2)

        #Ação necessária para manter rodando se o PP acabar
        if acabouPP is True:
            print('Sem PP')
            if Achar_Imagem_Tela('poke_center'):
                time.sleep(2)
                Clicar_Imagem('poke_center')
                print('Entrando Poke Center')
                time.sleep(2)
                Clicar_Imagem('heal')
                print('Curando ~~')
                time.sleep(2)
                if Achar_Imagem_Tela('heal_success'):
                    acabouPP = False
                    contador_pp = 0
                    print('Pokemons curados com sucesso!')
                    time.sleep(2)
        #Monitorando PP
        while acabouPP is False:
            #Clicar no "Ataque", no topo da tela
            Clicar_Imagem('ataque_Topo')
            print('Indo Atacar')
            #Clicar na grama
            Clicar_Imagem('grama')
            print('Começando a Luta')
            #Validando se o atacar está lá
            while not Achar_Imagem_Tela('fainted'):
                print('Pokémon vivo!')
                if Achar_Imagem_Tela('botao_atacar'):
                    #Clicar no Atacar para selecionar skill
                    Clicar_Imagem('botao_atacar')
                    print('Atacar!')
                    #Validando se tem PP
                    if contador_pp >= pp_total:
                        acabouPP = True
                        #Respirar
                        time.sleep(np.random.uniform(2,3))
                        #Clicar na skill securandária
                        print('Acabou PP, usando habilidade secundaria')
                        Clicar_Imagem('fire_fang')
                        #Setar que acabou PP
                        time.sleep(np.random.uniform(2,3))
                    #Se não acabou o PP, mantem na primeira habilidade
                    else:
                        Clicar_Imagem('flamethrower')
                        contador_pp += (np.random.uniform(1,2))
                        print('Usando habilidade')
                        time.sleep(np.random.uniform(2,3))