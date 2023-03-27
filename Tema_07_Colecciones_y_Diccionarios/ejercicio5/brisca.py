"""
        Ejercicio 5:

            Escribe un programa que genere una secuencia de 5 cartas de la baraja española y que sume los puntos según
            el juego de la brisca. El valor de las cartas se debe guardar en un diccionario que debe contener parejas
            (figura, valor), por ejemplo (“caballo”, 3). La secuencia de cartas debe ser una lista que contiene objetos
            de la clase Carta. El valor de las cartas es el siguiente: as → 11, tres → 10, sota → 2, caballo → 3,
            rey → 4; el resto de cartas no vale nada.



    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

import random
from Tema_06_POO.Tanda3POO.ejercicio14.card import Card


def main():
    mini_diccionario_briscas = {"AS": 11, "3": 10, "SOTA": 2, "CABALLO": 3, "REY": 4}
    PALOS = "BASTOS COPAS ESPADAS OROS".split()
    NUMEROS = "AS 2 3 4 5 6 7 SOTA CABALLO REY".split()
    NUMERO_CARTAS = 5
    puntuacion_total = 0

    lista_cartas = []
    while len(lista_cartas) < NUMERO_CARTAS:
        carta = Card(random.choice(PALOS), random.choice(NUMEROS))
        if carta in lista_cartas:
            continue
        else:
            punto_carta = mini_diccionario_briscas.get(carta.valor, 0)
            puntuacion_total += punto_carta
            lista_cartas.append(carta)
            print(f"La carta: {carta} puntua: {punto_carta}")

    print(f"Puntuación total: {puntuacion_total}")


if __name__ == "__main__":
    main()
