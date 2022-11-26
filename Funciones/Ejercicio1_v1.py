"""
    Ejercicio 1 v.1:

        Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cuatro opciones: sumar,
        restar, multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables
        y muestra el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error.

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


SALIDA_CON_EXITO = 1
ERROR_DIVIDE_0 = 2

numero_a = int(input("Introduce el valor A: "))
numero_b = int(input("Introduce el valor B: "))

while True:
    sleep(1.5)
    print("Menu de opciones:")
    print("Selecciona una de las siguientes opciones:   ")
    print('1. Sumar.')
    print('2. Restar.')
    print('3. Multiplicar.')
    print('4. Dividir.')
    print('5. Terminar.')
    print('-------------------------------------------------')
    opcion = int(input("¿Que vas a selecionar?    "))
    match opcion:
        case 1:
            resultado = suma(numero_a, numero_b)
            print(f"El resultado de sumar {numero_a} + {numero_b} es {resultado}")
        case 2:
            resultado = resta(numero_a, numero_b)
            print(f"El resultado de restar {numero_a} - {numero_b} es {resultado}")
        case 3:
            resultado = multiplica(numero_a, numero_b)
            print(f"El resultado de restar {numero_a} * {numero_b} es {resultado}")
        case 4:
            resultado = divide(numero_a, numero_b)
            print(f"El resultado de restar {numero_a} / {numero_b} es {resultado}")
        case 5:
            sleep(1.55)
            print('Has salido del programa con éxito.', file=sys.stderr)
            sys.exit(SALIDA_CON_EXITO)
        case _:
            print("La opcion no es correcta, vuelve a intentarlo")
            continue
