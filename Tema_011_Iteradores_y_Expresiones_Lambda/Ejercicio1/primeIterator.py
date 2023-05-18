"""
        Ejercicio 1:
            Crea el iterador PrimeIterator que permita iterar sobre la lista de números primos, desde 2 hasta uno dado
            como máximo.

            Ejemplo: "primes = list(PrimeIterator(15)) devolverá [2, 3, 5, 7, 11, 13]
    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import math
from collections.abc import Iterator


class PrimeIterator(Iterator):
    def __init__(self, num):
        if num < 2:
            raise ValueError("No puede ser menor que 2")
        self.__num = num
        self.__primo = 0

    @property
    def num(self):
        return self.__num

    @property
    def primo(self):
        return self.__primo

    def __next__(self):
        while True:
            self.__primo += 1
            if self.__primo > self.__num:
                raise StopIteration
            if self.__es_primo(self.__primo):
                return self.__primo

    @staticmethod
    def __es_primo(numero):
        if numero <= 1:
            return False
        for divisor in range(2, int(math.sqrt(numero)) + 1):
            if numero % divisor == 0:
                return False
        return True
