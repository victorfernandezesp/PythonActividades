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

# Sumamos filas
for x in range(cant_num_x):  # Se recorren las Filas
    print(f"La suma de la fila {x} es: {sum(matriz[x])}")  # Utilizamos la funcion sum() para sumar la fila concreta

# Sumamos Columnas
# Se recorren las Columnas externamente porque nos vamos a mover entre columnas.
# No nos vamos a mover entre filas ya que vamos a sumar entre columnas, no entre filas
for y in range(cant_num_y):
    suma = 0                        # Cargamos la variable suma a 0 para limpiar de valores de las próximas operaciones.
    for x in range(cant_num_x):     # Se recorren las filas internamente para movernos entre las columnas.
        suma += matriz[x][y]        # Guardamos en la variable suma el valor en la posicion [x][y] de la MATRIZ
    print(f"La suma de la columna {y} es: {suma}")      # Mostramos la matriz
