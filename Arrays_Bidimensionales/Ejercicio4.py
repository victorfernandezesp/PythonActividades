"""
    Ejercicio 4:

        Realiza un programa que rellene un array de 6 filas por 10 columnas con números enteros positivos comprendidos
        entre 0 y 1000 (ambos incluidos). A continuación, el programa deberá dar la posición tanto del máximo como del
        mínimo.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from random import randrange

filas = 6
columnas = 10

matriz = [[0] * columnas for _ in range(filas)]
for x in range(filas):
    for y in range(columnas):
        matriz[x][y] = randrange(0, 1000)

candidato = 0
for x in range(filas):
    for y in range(columnas):
        print("%5d   " % (matriz[x][y]), end=" ")
    print("")
