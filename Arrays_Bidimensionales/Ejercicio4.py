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
posicion_x_maximo = 0
posicion_y_maximo = 0
posicion_x_minimo = 0
posicion_y_minimo = 0
mayor = 0
menor = 1000

matriz = [[0] * columnas for _ in range(filas)]
for x in range(filas):
    for y in range(columnas):
        matriz[x][y] = randrange(0, 1001)
        if mayor < matriz[x][y]:
            mayor = matriz[x][y]
            posicion_x_maximo = x
            posicion_y_maximo = y
        if menor > matriz[x][y]:
            menor = matriz[x][y]
            posicion_x_minimo = x
            posicion_y_minimo = y

for x in range(filas):
    for y in range(columnas):
        print("%4d   " % (matriz[x][y]), end=" ")
    print("")

print(f"El mayor de la matriz es: {mayor} que esta en la posicion ({posicion_x_maximo}, {posicion_y_maximo})")
print(f"El menor de la matriz es: {menor} que esta en la posicion ({posicion_x_minimo}, {posicion_y_minimo})")