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
import random
from typing import List
from typeguard import typechecked
from Tema_06_POO.Tanda3POO.ejercicio14.card import Card


@typechecked
class Deck:
    def __init__(self, *cartas: List[Card]):
        self.__baraja = list(cartas)
        self.barajar_cartas()

    @property
    def tamano(self):
        return len(self.__cards)

    def reparte_cartas(self, jugador, num_cartas: int):
        lista_de_cartas_a_repartir = []
        for i in range(num_cartas):
            carta_sacada = self.__baraja.pop(0)
            lista_de_cartas_a_repartir.append(carta_sacada)
        jugador.recives(lista_de_cartas_a_repartir)

    def robar_carta(self):
        if self.tamano == 0:
            raise ValueError("No quedan cartas en la baraja")
        return self.baraja.pop(0)

    def barajar_cartas(self):
        random.shuffle(self.__baraja)

    def __repr__(self):
        return f"{self.__class__.__name__} Baraja: {self.__baraja}"
