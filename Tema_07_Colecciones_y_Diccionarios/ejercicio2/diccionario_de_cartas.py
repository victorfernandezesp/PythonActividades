"""
        Ejercicio 2:

            Realiza un programa que escoja al azar 10 cartas de la baraja española (10 objetos de la clase Carta).
            Emplea una lista para almacenarlas y asegúrate de que no se repite ninguna. Las cartas se deben mostrar
            ordenadas. Primero se ordenarán por palo (bastos, copas, espadas, oros) y cuando coincida el palo, se
            ordenará por número: as, 2, 3, 4, 5, 6, 7, sota, caballo, rey.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import random
from Tema_06_POO.Tanda3POO.ejercicio14.card import Card


def main():
    PALOS = "BASTOS COPAS ESPADAS OROS".split()
    NUMEROS = "AS 2 3 4 5 6 7 SOTA CABALLO REY".split()
    NUMERO_CARTAS = 10

    lista_cartas = []
    while len(lista_cartas) < NUMERO_CARTAS:
        carta = Card(random.choice(PALOS), random.choice(NUMEROS))
        if carta not in lista_cartas:
            lista_cartas.append(carta)
        else:
            continue

    lista_cartas.sort(key=lambda c: (c.palo, NUMEROS.index(c.valor)))

    for i in lista_cartas:
        print(i)


if __name__ == "__main__":
    main()
