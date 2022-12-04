from random import randrange


def crea_array_comprendido(minimo, maximo):
    array = []
    for i in range(minimo, maximo + 1):
        array.append(i)
    return array


def crea_array_comprendido_random(minimo, maximo, longitud):
    array = []
    for i in range(longitud):
        array.append(randrange(minimo, maximo))
    return array


def crea_array():
    longitud = int(input("¿Cuál va a ser la longitud de tu array?   "))
    array = []
    for i in range(longitud):
        array.append(int(input(f"Inserte el numero en la posicion {i}/{longitud - 1}:    ")))
    return array
