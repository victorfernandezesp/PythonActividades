"""
    Ejercicio 1:
    Crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6 que tienen la misma
    probabilidad de salir y un programa de prueba.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from random import randrange


class Dado:
    def __init__(self):
        self.__cara = 0

    def tirar_dado(self):
        cara_salida = randrange(1, 6)
        self.__cara = cara_salida
        return cara_salida

    def __str__(self):
        return f"El numero que ha salido es: {self.__cara}"
