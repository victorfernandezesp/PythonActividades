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
from typeguard import typechecked


@typechecked
class Card:
    def __init__(self, palo: str, valor: str):
        self.__palo = palo
        self.__valor = valor

    @property
    def palo(self):
        return self.__palo

    @property
    def valor(self):
        return self.__valor

    def __repr__(self):
        return f"{self.__class__.__name__} Palo: {self.__palo} Valor: {self.__valor}"
