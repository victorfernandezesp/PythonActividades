"""
    Ejercicio 4:
        Implementar otra clase Dado. Por defecto el dado tendrá 6 caras. Tendremos tres formas de construir un dado (uno
        al que no se le pasa nada e inicializa el dado al azar, otro al que solo se le pasa que número tiene el dado en
        la cara superior y otro con el número del dado en la cara superior y el número de caras del dado). Implementa
        los getters, el método roll() que tirará el dado al azar y el __str__(). Implementa un tester que tenga un
        vector de 4 dados y los lance una serie de veces.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from random import randrange

from typeguard import typechecked


class Dado:
    @typechecked
    def __init__(self, cara_superior: int = 0, caras: int = 6):
        self.cara_superior = cara_superior
        self.caras = caras

    @property
    def caras(self):
        return self.__caras

    @property
    def cara_superior(self):
        return self.__cara_superior

    @caras.setter
    @typechecked
    def caras(self, value: int):
        self.__caras = value

    @cara_superior.setter
    @typechecked
    def cara_superior(self, value: int):
        self.__cara_superior = value

    def roll(self):
        self.__cara_superior = randrange(1, self.caras)
        return self.__cara_superior

    def __str__(self):
        return f"Ha salido {self.__cara_superior}"

    def __repr__(self):
        return f"{self.__class__.__name__}(Ha salido {self.__cara_superior})"
