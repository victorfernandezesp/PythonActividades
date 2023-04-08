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

from Tema_06_POO.Tanda3POO.ejercicio14.card import Card

from Tema_06_POO.Tanda3POO.ejercicio14.deck import Deck

from Tema_06_POO.Tanda3POO.ejercicio14.card_player import Card_player

"""from Tema_06_POO.Tanda3POO.ejercicio14.baraja_espanola import SpanishDeck

from Tema_06_POO.Tanda3POO.ejercicio14.baraja_inglesa import EnglishDeck"""

Bastos1 = Card("Bastos", 1)
Bastos2 = Card("Bastos", 2)
Bastos3 = Card("Bastos", 3)
Bastos4 = Card("Bastos", 4)
Bastos5 = Card("Bastos", 5)
Bastos6 = Card("Bastos", 6)
Bastos7 = Card("Bastos", 7)
Bastos8 = Card("Bastos", 8)
Bastos9 = Card("Bastos", 9)
Bastos10 = Card("Bastos", 10)
Bastos11 = Card("Bastos", 11)
Bastos12 = Card("Bastos", 12)

"""baraja_simple = Deck(Bastos1, Bastos2, Bastos3, Bastos4, Bastos5, Bastos6, Bastos7, Bastos8, Bastos9, Bastos10,
                     Bastos11, Bastos12)
print(baraja_simple)"""

jugador1 = Card_player()

jugador1.robar_carta_baraja()
print(jugador1.cartas_de_jugador)

jugador1.recibir_cartas(2)
print(jugador1.cartas_de_jugador)

jugador1.tirar_carta("Bastos1")
print(jugador1.cartas_de_jugador)