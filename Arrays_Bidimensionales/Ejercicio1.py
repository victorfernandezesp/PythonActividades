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