"""
        Ejercicio 2:
        Haz el ejercicio anterior usando una lista interna y eliminando elementos con el algoritmo de la criba de
        Eratóstenes.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from collections.abc import Iterator

class PrimeIterator(Iterator):

    def __init__(self, num_tope):
        self.__num_tope = num_tope
        self.__lista_de_numeros = list(range(2, num_tope+1))
        self.__contador = 0
        self.__lista_de_numeros = self.__criba_eratostenes(self.__lista_de_numeros, self.__contador, self.__num_tope)
        self.__primo_iterador = iter(self.__lista_de_numeros)

    def __next__(self):
        return next(self.__primo_iterador)

    @staticmethod
    def __criba_eratostenes(lista, puntero, tope):
        while True:
            numero = lista[puntero]
            if numero ** 2 > tope:
                break
            for i in lista:
                if i is not numero and i % numero == 0:
                    lista.remove(i)
            puntero += 1
        return lista