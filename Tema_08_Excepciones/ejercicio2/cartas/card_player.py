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
from typing import List

from typeguard import typechecked

from Tema_06_POO.Tanda3POO.ejercicio14.card import Card

from Tema_06_POO.Tanda3POO.ejercicio14.deck import Deck


class Carta_No_Existe(TypeError):

    def __init__(self, carta):
        super().__init__(f"La carta no esta en tu baraja. Recibido: {carta}")
        self.carta = carta


@typechecked
class Card_player:
    def __init__(self):
        self.__cartas_de_jugador = []

    @property
    def cartas_de_jugador(self):
        return self.__cartas_de_jugador

    def robar_carta_baraja(self):
        carta = Deck.robar_carta()
        self.cartas_de_jugador.append(carta)

    def tirar_carta(self, carta: Card):
        if carta not in self.__cartas_de_jugador:
            raise Carta_No_Existe(carta)
        self.cartas_de_jugador.remove(carta)

    def recibir_cartas(self, cartas: List[Card]):
        self.cartas_de_jugador.extend(cartas)

    def __repr__(self):
        return f"{self.__class__.__name__} Cartas del jugador: {self.cartas_de_jugador} "
