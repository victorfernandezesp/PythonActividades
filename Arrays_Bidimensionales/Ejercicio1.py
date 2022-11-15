"""
    Ejercicio 1:

        Escribe un programa que pida 20 números enteros. Estos números se deben introducir en un array de 4 filas por 5
        columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se
        tratara. La suma total debe aparecer en la esquina inferior derecha.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
filas = 4
columnas = 5

matriz = [[0] * columnas for _ in range(filas)]
for x in range(filas):
    for y in range(columnas):
        matriz[x][y] = int(input(f"Fila {x}, Columna {y}:   "))

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
