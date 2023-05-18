"""
        Ejercicio 1:
            Crea el iterador PrimeIterator que permita iterar sobre la lista de números primos, desde 2 hasta uno dado
            como máximo.

            Ejemplo: "primes = list(PrimeIterator(15)) devolverá [2, 3, 5, 7, 11, 13]
    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from Tema_011_Iteradores_y_Expresiones_Lambda.Ejercicio1.primeIterator import PrimeIterator

primes = list(PrimeIterator(15))
print(primes)

