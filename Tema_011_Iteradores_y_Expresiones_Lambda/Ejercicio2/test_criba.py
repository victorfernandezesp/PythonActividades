"""
        Ejercicio 2:
        Haz el ejercicio anterior usando una lista interna y eliminando elementos con el algoritmo de la criba de
        Eratóstenes.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from Tema_011_Iteradores_y_Expresiones_Lambda.Ejercicio2.criba_de_Eratostenes import PrimeIterator

primes = list(PrimeIterator(50))
print(primes)

