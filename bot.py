import psutil
from controls import *
from pyautogui import *
import time
import numpy as np
import keyboard
from multiprocessing import Process

#Colocando botão para ligar/parar
def bot():
    # Esperar um pouco para iniciar, vulgo dar alt tab 
    time.sleep(5)

    acabouPP = False
    pp_total = 15
    contador_pp = 0
    captcha = False
    count_battles = 0
    
    while True:
        time.sleep(1)
        while checar_captcha() is False:
            print('Preparando para Iniciar')
            if Achar_Imagem_Tela('poke_center'):
                time.sleep(2)
                print('Entrando Poke Center')
                Clicar_Imagem('poke_center')
                time.sleep(2)
                print('Curando ~~')
                Clicar_Imagem('heal')
                time.sleep(2)
                if Achar_Imagem_Tela('heal_success'):
                    acabouPP = False
                    contador_pp = 0
                    print('Pokemons curados com sucesso!')
                    time.sleep(2)
            #Ação necessária para manter rodando se o PP acabar
            if acabouPP is True:
                print('Sem PP')
                if Achar_Imagem_Tela('poke_center') and checar_captcha() is False:
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
            while acabouPP is False and checar_captcha() is False:
                #Clicar no "Ataque", no topo da tela
                Clicar_Imagem('ataque_Topo')
                print('Indo Atacar')
                time.sleep(2)
                #Clicar na grama
                if checar_captcha() is False:
                    Clicar_Imagem('grama')
                    count_battles += 1
                    print('Foram iniciadas ' + str(count_battles) + ' batalhas')
                    print('Começando a Luta')
                #Validando se o atacar está lá
                while not Achar_Imagem_Tela('fainted') and checar_captcha() is False and Achar_Imagem_Tela('in_battle') is True:
                    print('Batalhando!')
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
        resolver_captcha()

#função para pausar
if __name__ == '__main__':
    p = Process(target=bot, daemon=True)
    p.start()
    util = psutil.Process(p.pid)
    running = True
    while True:
        time.sleep(0.1)
        if keyboard.is_pressed('q') and not running:
            print('Resuming')
            util.resume()
            running = True
        elif keyboard.is_pressed('q') and running:
            print('Suspended')
            util.suspend()
            running = False     