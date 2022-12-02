""" Ejercicio 19.
        Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes
        correspondiente.


    Author: Victor Fernandez España
    Curso:  2022-2003
"""
import sys

NUMERO_MES_ERROR = 1
print("Este programa te dice los dias del mes introduciendo el numero de mes ")

numero_mes = int(input("Introduce el numero del mes, por favor! "))
if 0 > numero_mes or numero_mes > 12:
    print(f"ERROR. Tiene que ser un numero entre 1 y 12 ", file=sys.stderr)
    sys.exit(NUMERO_MES_ERROR)

match numero_mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"El mes {numero_mes} tiene 31 días ")
    case 2:
        es_bisiesto = input("¿Es bisiesto? Si es bisiesto introduce un S: ")
        if es_bisiesto == "S":
            print(f"El mes {numero_mes} tiene 29 días ")
        else:
            print(f"El mes {numero_mes} tiene 28 días ")

    case 4 | 6 | 9 | 11:
        print(f"El mes {numero_mes} tiene 30 días ")
