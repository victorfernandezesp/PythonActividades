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

for x in range(cant_num_x):      # Recorremos las filas externas porque nos moveremos entre filas cuando una este llena
    vector = []                  # Inicializamos el vector que nos servirá también para limpiar el contenido
    for y in range(cant_num_y):  # Recorremos las columnas intern. porque nos moveremos entre columnas cuando este llena
        auxiliar = int(input(f"Fila {x}, Columna {y}:   "))  # Guardamos en una var. el entero de pedir en una pos. x y
        vector.append(auxiliar)  # Guardamos en el vector el valor
    matriz.append(vector)        # Guardamos en la matriz el vector, nuestra matriz esta formado por vectores


# Mostramos la matriz con un formato mas visual y bonito

for filas in matriz:
    print("[", end=" ")
    for elemento in filas:
        print("{:8.0f}".format(elemento), end=" ")
    print("]")