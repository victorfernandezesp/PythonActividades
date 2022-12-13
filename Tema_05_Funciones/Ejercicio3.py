"""
    Ejercicio 3:
        Crea una biblioteca de funciones (statistics) dentro de un paquete (util) que contenga las siguientes funciones:

        maximum
        recibiendo como parámetro un array de enteros
        recibiendo un conjunto de parámetros enteros

        minimum
        recibiendo como parámetro un array de enteros
        recibiendo un conjunto de parámetros enteros

        mean
        recibiendo como parámetro un array de enteros
        recibiendo un conjunto de parámetros enteros

        variance
        recibiendo como parámetro un array de enteros y haciendo uso de la función anterior
        recibiendo un conjunto de parámetros enteros y haciendo uso de la función anterior

        median
        recibiendo como parámetro un array de enteros
        recibiendo un conjunto de parámetros enteros

        mode
        recibiendo como parámetro un array de enteros
        recibiendo un conjunto de parámetros enteros
        devuelve un array de enteros (puede haber varias modas)

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from Tema_05_Funciones.util.statistics import maximum, minimum, mean, \
    variance, median, mode


def longitud():
    longitud_vectorarray = int(input("¿Cuál va a ser la longitud de tu array?:    "))
    return longitud_vectorarray


def rellena_array(longi):
    vector = []
    for i in range(longi):
        vector.append(int(input(f"Inserte el numero en la posicion {i}/{longi - 1}:    ")))
    return vector


longitud_vector = (longitud())
array = rellena_array(longitud_vector)
print(f"El maximo es: {maximum(array)}")
print(f"El minimo es: {minimum(array)}")
print(f"La media es: {mean(array)}")
print(f"La varianza es: {variance(array)}")
print(f"La mediana es: {median(array)}")
if len(mode(array)) < 2:
    print(f"La moda es: {mode(array)}")
else:
    print(f"Las modas son: {mode(array)}")
