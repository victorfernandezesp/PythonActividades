"""
    Ejercicio 1 v.1:

        Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cuatro opciones: sumar,
        restar, multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables
        y muestra el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error.

        Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera).
        Las variables se inicializan a cero.

        Modifica el programa anterior para que si no se introducen las dos
        variables desde la opción correspondiente no se puedan ejecutar el resto de las opciones.

        Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas, pide una opción
        (por su número) y devuelve la opción escogida. Modifica el último programa para que use esta función.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys
from time import sleep

from bibliotecafunciones.funciones_menu.menu import menu
from bibliotecafunciones.funciones_menu.menu import opcion_escogida


def suma(a, b):
    c = a + b
    return c


def resta(a, b):
    c = a - b
    return c


def multiplica(a, b):
    c = a * b
    return c


def divide(a, b):
    if b != 0:
        c = a / b
        return c
    else:
        print("No puedes dividir por 0", file=sys.stderr)
        sys.exit(ERROR_DIVIDE_0)


def introduce_parametro():
    x = int(input("Introduce el valor:  "))
    return x


SALIDA_CON_EXITO = 1
ERROR_DIVIDE_0 = 2

numero_a = 0
numero_b = 0

parametros_introducido = False
vector_menu = ["Introducir los parametros", "Sumar", "Restar", "Multiplicar", "Dividir", "Terminar"]

while True:
    sleep(0.5)
    menu(vector_menu)
    opcion = opcion_escogida()
    match opcion:
        case 1:
            numero_a = introduce_parametro()
            numero_b = introduce_parametro()
            parametros_introducido = True

        case 2:
            if parametros_introducido:
                resultado = suma(numero_a, numero_b)
                print(f"El resultado de sumar {numero_a} + {numero_b} es {resultado}")
            else:
                print("Primero tienes que introducir los parametros, selecciona la opcion 1")

        case 3:
            if parametros_introducido:
                resultado = resta(numero_a, numero_b)
                print(f"El resultado de restar {numero_a} - {numero_b} es {resultado}")
            else:
                print("Primero tienes que introducir los parametros, selecciona la opcion 1")

        case 4:
            if parametros_introducido:
                resultado = multiplica(numero_a, numero_b)
                print(f"El resultado de restar {numero_a} * {numero_b} es {resultado}")
            else:
                print("Primero tienes que introducir los parametros, selecciona la opcion 1")

        case 5:
            if parametros_introducido:
                resultado = divide(numero_a, numero_b)
                print(f"El resultado de restar {numero_a} / {numero_b} es {resultado}")
            else:
                print("Primero tienes que introducir los parametros, selecciona la opcion 1")
        case 6:
            sleep(1.55)
            print('Has salido del programa con éxito.', file=sys.stderr)
            sys.exit(SALIDA_CON_EXITO)

        case _:
            print("La opcion no es correcta, vuelve a intentarlo")
            continue