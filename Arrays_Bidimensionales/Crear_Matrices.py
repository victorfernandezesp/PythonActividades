"""
    Crear Matrices:
        Este programa crea matrices 2D, y la muestra con un formato determinado para su correcta previsualización

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

matriz = []
cant_num_x = int(input("Cuantas Filas (x) va a contener el array que quieres que sume?:          "))
cant_num_y = int(input("Cuantos Columnas (y) va a contener el array que quieres que sume?:       "))

# Creamos la Matriz
for x in range(cant_num_x):
    vector = []
    for y in range(cant_num_y):
        auxiliar = int(input(f"Fila {x}, Columna {y}:   "))
        vector.append(auxiliar)
    matriz.append(vector)


for filas in matriz:
    print("[", end=" ")
    for elemento in filas:
        print("{:8.0f}".format(elemento), end=" ")
    print("]")