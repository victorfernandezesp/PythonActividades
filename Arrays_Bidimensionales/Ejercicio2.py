"""
    Ejercicio 2:

        Modifica el programa anterior de tal forma que los números que se introducen en el array se generen de forma
        aleatoria (valores entre 100 y 999).

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from random import randrange
filas = 4
columnas = 5

matriz = [[0] * columnas for _ in range(filas)]
for x in range(filas):
    for y in range(columnas):
        matriz[x][y] = randrange(100, 999)

for x in range(filas):
    for y in range(columnas):
        print("%7d   " % (matriz[x][y]), end="")
    print(" | %7d" % sum(matriz[x]))

for y in range(columnas):
    print("___________", end="")
print("___________")
suma_total = 0
for y in range(columnas):
    suma_columna = 0
    for x in range(filas):
        suma_columna += matriz[x][y]
    suma_total += suma_columna
    print("%7d   " % suma_columna, end="")
print(" | %7d   " % suma_total)
