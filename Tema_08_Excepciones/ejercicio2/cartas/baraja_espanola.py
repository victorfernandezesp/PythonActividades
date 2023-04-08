"""
        Ejercicio 14:

            Crea en Python las siguientes clases:

            --Card que simule una carta de naipes. Un naipe tiene un palo (de un conjunto de palos) y un valor (de un
            conjunto de valores).

            --CardPlayer que simule un jugador de naipes. Un jugador tiene un conjunto de naipes.

                Puede robar una carta de una baraja.
                Una vez robada el jugador tiene una carta más y la baraja una menos.
                Puede deshacerse de una carta.
                Puede recibir cartas.

            --Deck que simula un conjunto de cartas de naipes.
                Inicialmente, tiene las cartas que le llegan con el constructor.
                Puede repartir un conjunto de cartas a un jugador. En la baraja dejan de existir esas cartas.
                Le pueden quitar la primera carta (robar).
                Puede barajarse.

            --Baraja Española e Inglesa (SpanishDeck e EnglishDeck) que heredan de Deck.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from Tema_06_POO.Tanda3POO.ejercicio14.deck import Deck
from Tema_06_POO.Tanda3POO.ejercicio14.card import Card


class SpanishDeck(Deck):

    def __init__(self):
        numeros = "1 2 3 4 5 6 7 8 9 SOTA CABALLO REY".split()
        palos = "OROS COPAS ESPADAS BASTOS".split()
        cartas = [Card(n, s) for s in palos for n in numeros]
        super().__init__(cartas)
