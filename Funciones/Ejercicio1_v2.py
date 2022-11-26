"""
    Ejercicio 1 v.2:

        Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cuatro opciones: sumar,
        restar, multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables
        y muestra el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error.

        Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera).
        Las variables se inicializan a cero.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys
from time import sleep


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

while True:
    sleep(0.5)
    print("Menu de opciones:")
    print("Selecciona una de las siguientes opciones:   ")
    print('1. Introduce los parametros.')
    print('2. Sumar.')
    print('3. Restar.')
    print('4. Multiplicar.')
    print('5. Dividir.')
    print('6. Terminar.')
    print('-----------------------------------------------------------------------------------------------------------')
    opcion = int(input("¿Que vas a selecionar?    "))
    match opcion:
        case 1:
            numero_a = introduce_parametro()
            numero_b = introduce_parametro()

        case 2:
            resultado = suma(numero_a, numero_b)
            print(f"El resultado de sumar {numero_a} + {numero_b} es {resultado}")
        case 3:
            resultado = resta(numero_a, numero_b)
            print(f"El resultado de restar {numero_a} - {numero_b} es {resultado}")
        case 4:
            resultado = multiplica(numero_a, numero_b)
            print(f"El resultado de restar {numero_a} * {numero_b} es {resultado}")
        case 5:
            resultado = divide(numero_a, numero_b)
            print(f"El resultado de restar {numero_a} / {numero_b} es {resultado}")
        case 6:
            sleep(1.55)
            print('Has salido del programa con éxito.', file=sys.stderr)
            sys.exit(SALIDA_CON_EXITO)
        case _:
            print("La opcion no es correcta, vuelve a intentarlo")
            continue
