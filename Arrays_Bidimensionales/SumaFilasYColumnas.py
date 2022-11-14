"""
    Ejercicio 1:

        Escribe un programa que pida 20 números enteros. Estos números se deben introducir en un array de 4 filas por 5
        columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se
        tratara. La suma total debe aparecer en la esquina inferior derecha.

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

for x in range(cant_num_x):
    print(f"La suma de la fila {x} es: {sum(matriz[x])}")

for y in range(cant_num_y):
    suma = 0
    for x in range(cant_num_x):
        suma += matriz[x][y]
    print(f"La suma de la columna {y} es: {suma}")
