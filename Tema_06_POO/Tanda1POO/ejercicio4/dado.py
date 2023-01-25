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

CARAS_POR_DEFECTO = 6


class Dado:
    @typechecked
    def __init__(self, cara_superior: int = 0, caras: int = CARAS_POR_DEFECTO):

        if caras <= 0:
            raise ValueError(f"El número de caras del dado no puede ser menor a cero. Recibido: {caras}")

        self.__caras = caras

        if cara_superior < 0 or cara_superior > caras:
            raise ValueError((f"No se le puede asignar al dado un valor menor a cero o mayor que el número de caras. "
                              f"Recibido: {cara_superior}"))

        if cara_superior == 0:
            self.roll()
        else:
            self.__cara_superior = cara_superior

    @property
    def caras(self):
        return self.__caras

    @property
    def cara_superior(self):
        return self.__cara_superior

    def roll(self):
        self.__cara_superior = randrange(1, self.caras)
        return self.__cara_superior

    def __str__(self):
        return f"{self.__cara_superior}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__cara_superior})"
