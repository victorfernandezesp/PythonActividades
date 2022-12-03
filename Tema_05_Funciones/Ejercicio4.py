"""
    Ejercicio 4:
        Haz un programa que muestre un menú y, usando las funciones anteriores, ejecute las siguientes opciones:
        
        Muestra los números primos que hay entre 1 y 1000.
        Muestra los números capicúa que hay entre 1 y 99999.
        Muestra la moda de 50 números enteros aleatorios entre 1 y 10.
        Muestra la mediana de 10 números enteros aleatorios entre 1 y 50.
        Muestra el máximo y mínimo de 1000 números enteros aleatorios entre 1 y 50000.
        Muestra la varianza de 10 números enteros aleatorios entre 1 y 5.
        
    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys
from time import sleep

from bibliotecafunciones.funciones_matematicas.crea_array_de_n_parametros_comprendidos import crea_array_comprendido, \
    crea_array_comprendido_random

from bibliotecafunciones.funciones_matematicas.funciones_matematicas_tema05_ej2 import es_primo, es_capicua

from bibliotecafunciones.funciones_menu.menu import menu, opcion_escogida

from util.statistics import mode, median, minimum, maximum

SALIDA_PROGRAMA = 1
MINIMO_CASO_1 = 1
MAXIMO_CASO_1 = 1000
MINIMO_CASO_2 = 1
MAXIMO_CASO_2 = 99999
MINIMO_CASO_3 = 1
MAXIMO_CASO_3 = 10
LONGITUD_CASO_3 = 50
MINIMO_CASO_4 = 1
MAXIMO_CASO_4 = 50
LONGITUD_CASO_4 = 10
MINIMO_CASO_5 = 1
MAXIMO_CASO_5 = 50000
LONGITUD_CASO_5 = 1000
MINIMO_CASO_6 = 1
MAXIMO_CASO_6 = 5
LONGITUD_CASO_6 = 10

vector_menu = ["Muestra los números primos que hay entre 1 y 1000.",
               "Muestra los números capicúa que hay entre 1 y 99999.",
               "Muestra la moda de 50 números enteros aleatorios entre 1 y 10.",
               "Muestra la mediana de 10 números enteros aleatorios entre 1 y 50.",
               "Muestra el máximo y mínimo de 1000 números enteros aleatorios entre 1 y 50000.",
               "Muestra la varianza de 10 números enteros aleatorios entre 1 y 5.",
               "Salir del programa."]
while True:
    sleep(0.5)
    menu(vector_menu)
    opcion = opcion_escogida()
    match opcion:

        case 1:
            array = crea_array_comprendido(MINIMO_CASO_1, MAXIMO_CASO_1)

            for i in range(len(array)):
                if es_primo(array[i]):
                    print(f"{array[i]},", end=" ")
            print("     ")

        case 2:
            array = crea_array_comprendido(MINIMO_CASO_2, MAXIMO_CASO_2)

            for i in range(len(array)):
                if es_capicua(array[i]):
                    print(f"{array[i]},", end=" ")
            print("     ")

        case 3:
            array = crea_array_comprendido_random(MINIMO_CASO_3, MAXIMO_CASO_3, LONGITUD_CASO_3)
            print(f"El array es: {array}")
            mode(array)
            if len(mode(array)) < 2:
                print(f"La moda es: {mode(array)}")
            else:
                print(f"Las modas son: {mode(array)}")

        case 4:
            array = crea_array_comprendido_random(MINIMO_CASO_4, MAXIMO_CASO_4, LONGITUD_CASO_4)
            print(f"El array es: {array}")
            print(f"La mediana es: {median(array)}")

        case 5:
            array = crea_array_comprendido_random(MINIMO_CASO_5, MAXIMO_CASO_5, LONGITUD_CASO_5)
            print(f"El array es: {array}")
            print(f"El mínimo es: {minimum(array)}")
            print(f"El máximo es: {maximum(array)}")

        case 6:
            array = crea_array_comprendido_random(MINIMO_CASO_6, MAXIMO_CASO_6, LONGITUD_CASO_6)
            print(f"El array es: {array}")
            print(f"La mediana es: {median(array)}")

        case 7:
            sleep(1.25)
            print('Has salido del programa.', file=sys.stderr)
            sys.exit(SALIDA_PROGRAMA)

        case _:
            print("La opcion no es correcta, vuelve a intentarlo")
            continue
