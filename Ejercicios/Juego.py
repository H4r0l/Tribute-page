import os
import time
clear = lambda: os.system('cls')
def lapso(x):
    time.sleep(1.0)
    print(x)
print("=" * 30)
lapso("Bienvendo a la isla! \n Tu mision será encontrar el tesoro")
print("=" * 30)
respuesta = int(input("Has encontrado dos caminos, ¿Por cual sigues? \n 1. Izquierda \n 2. Derecha\n"))
clear()
if(respuesta == 1):
    lapso("Te has encontrado un lago\n")
    lapso("Hay un Cocodrilo obstaculizando uno de los caminos, puedes esperar a que se vaya o nadar\n")
    respuesta = int(input("¿Nadas o esperas?:\n 1. Esperar\n 2. Nadar\n"))
    clear()
    if(respuesta == 1):
        lapso("Encontraste otro camino que te llevo hasta una cabaña\n")
        respuesta = int(input("¿Rodeas la casa o entras a la sala principal?\n1. Rodearla\n2. Entrar a la casa\n1"))
        clear()
        if(respuesta == 1):
            lapso("Caiste en una trampa\n Game over")
            exit()
        elif(respuesta == 2):
            lapso("Tienes tres puertas, ¿A cual entras?")
            respuesta = int(input("1. Roja\n2. Amarilla\n3. Azul\n"))
            if(respuesta == 1):
                lapso("Eres quemado\n Game over")
                exit()
            elif(respuesta == 2):
                lapso("Has ganado :D")
                exit()
            elif(respuesta == 3):
                lapso("Fuiste devorado por bestias\n Game over")
                exit()
        elif(respuesta == 2):
            lapso("Del otro lado te encuentras con una aldea\n")
            lapso("Eres atacado por una tribu\n Game over")
            exit()
elif(respuesta == 2):
    lapso("Has caido en un agujero\n Game over")
    exit()
