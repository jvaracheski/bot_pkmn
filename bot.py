from controls import *
from pyautogui import *
import time
import numpy as np
import keyboard
from multiprocessing import Process
import sys


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
        while not Achar_Imagem_Tela('captcha'):
            if captcha is False:
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
                        captcha = True
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
                count_battles += 1
                print('Foram iniciadas' + count_battles + ' batalhas')
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

#função para pausar
if __name__ == '__main__':
    p = Process(target=bot, daemon=True)
    p.start()
    while True:
        time.sleep(0.1)
        if keyboard.is_pressed('q'):
            p.terminate()
            print('Finalizando')
            sys.exit()