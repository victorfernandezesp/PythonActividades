"""
    Crear Matrices:
        Este programa crea matrices 2D, y la muestra con un formato determinado para su correcta previsualización

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

filas = int(input("Escribe el numero de filas:      "))
columnas = int(input("Escribe el numero de columnas:    "))
matriz = []

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = float(input("Fila {}, Columna {}:   ".format(i+1, j+1)))
        matriz[i].append(valor)

print()
for filas in matriz:
    print("[", end=" ")
    for elemento in filas:
        print("{:8.0f}".format(elemento), end=" ")
    print("]")