"""
    Ejercicio 3:

        Este programa juega al piedra/papel/tijera contra el ordenador que usa números aleatorios para realizar la
        tirada.
        Después de cada jugada pregunta al usuario si quiere continuar, en caso negativo se muestra el número de
        partidas jugadas, las ganadas por cada jugador y las empatadas.

    Autor: Víctor Fernández España
    Curso: 2022-2023

"""
from random import randrange
from time import sleep
partidas_jugadas = 0
partidas_ganadas = 0
partidas_empatadas = 0
partidas_perdidas = 0

while True:
    print("Selecciona 1 si vas a jugar Piedra.")
    print("Selecciona 2 si vas a jugar Papel.")
    print("Selecciona 3 si vas a jugar Tijera.")

    ordenador_selecciona = randrange(1, 3)
    seleccion = int(input("¿Que vas a sacar?: "))

    if seleccion < 1 or seleccion > 3:
        print(f"ERROR. Tienes que escoger Piedra(1), Papel(2) o Tijera(3) ")
        continue

    sleep(1)
    print("Piedra, Papel o Tijera")
    sleep(1)
    print("Una")
    sleep(1)
    print("Dos")
    sleep(1)
    print("Y Tres")
    sleep(1)
    match seleccion:
        case 1:
            if ordenador_selecciona == 3:
                print(f"Ganaste, la maquina ha sacado Tijera")
                partidas_ganadas += 1
            elif ordenador_selecciona == 2:
                print(f"Perdiste, la maquina ha sacado Papel")
                partidas_perdidas += 1
            else:
                print(f"Empate, la maquina ha sacado Piedra")
                partidas_empatadas += 1

        case 2:
            if ordenador_selecciona == 1:
                print(f"Ganaste, la maquina ha sacado Piedra")
                partidas_ganadas += 1
            elif ordenador_selecciona == 3:
                print(f"Perdiste, la maquina ha sacado Tijera")
                partidas_perdidas += 1
            else:
                print(f"Empate, la maquina ha sacado Papel")
                partidas_empatadas += 1

        case 3:
            if ordenador_selecciona == 2:
                print(f"Ganaste, la maquina ha sacado Papel")
                partidas_ganadas += 1
            elif ordenador_selecciona == 1:
                print(f"Perdiste, la maquina ha sacado Piedra")
                partidas_perdidas += 1
            else:
                print(f"Empate, la maquina ha sacado Tijera")
                partidas_empatadas += 1

    partidas_jugadas += 1

    seguir_jugando = input("¿Quieres seguir jugando? Si no quieres seguir jugando introduce 'N': ")
    if seguir_jugando == "N":
        print(f"Has jugado {partidas_jugadas}.")
        print(f"Has ganado {partidas_ganadas}.")
        print(f"Has empatado {partidas_empatadas}.")
        print(f"Has perdido {partidas_perdidas}.")
        break