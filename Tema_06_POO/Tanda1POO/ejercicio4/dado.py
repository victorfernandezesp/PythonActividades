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


class Dado:
    def __init__(self):
        self.cara_superior = 0
        self.caras = 6
        self.numero_salido = 0

    @property
    def caras(self):
        return self.__caras

    @property
    def cara_superior(self):
        return self.__cara_superior

    @property
    def numero_salido(self):
        return self.__numero_salido

    @caras.setter
    def caras(self, value):
        self.__caras = value

    @cara_superior.setter
    def cara_superior(self, value):
        self.__cara_superior = value

    def roll(self):
        self.numero_salido = randrange(1, self.caras)
        return self.__numero_salido

    @numero_salido.setter
    def numero_salido(self, value):
        self.__numero_salido = value

    def __str__(self):
        return f"Ha salido {self.__numero_salido}"