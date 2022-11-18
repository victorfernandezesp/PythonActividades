"""
    Ejercicio 1:

        Escribe un programa que pida 20 números enteros. Estos números se deben introducir en un array de 4 filas por 5
        columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se
        tratara. La suma total debe aparecer en la esquina inferior derecha.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
FILAS = 4
COLUMNAS = 5
matriz = [[0] * COLUMNAS for _ in range(FILAS)]
for x in range(FILAS):
    for y in range(COLUMNAS):
        matriz[x][y] = int(input(f"Fila {x}, Columna {y}:   "))

for x in range(FILAS):
    for y in range(COLUMNAS):
        print("%7d   " % (matriz[x][y]), end="")
    print(" | %7d" % sum(matriz[x]))

for y in range(COLUMNAS):
    print("___________", end="")
print("___________")
suma_total = 0
for y in range(COLUMNAS):
    suma_columna = 0
    for x in range(FILAS):
        suma_columna += matriz[x][y]
    suma_total += suma_columna
    print("%7d   " % suma_columna, end="")
print(" | %7d   " % suma_total)
