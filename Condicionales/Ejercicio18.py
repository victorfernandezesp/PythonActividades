""" Ejercicio 18.
        Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente.
        Si introducimos otro número nos da un error.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
import sys

NUMERO_DIA_ERROR = 1
print("Este programa te dice dia de la semana introduciendo el numero de dia ")

dia_semana = int(input("Introduce el numero del dia, por favor! "))
if 0 > dia_semana or dia_semana > 7:
    print(f"ERROR. Tiene que ser un numero entre 1 y 7 ", file=sys.stderr)
    sys.exit(NUMERO_DIA_ERROR)

match dia_semana:
    case 1:
        print(f"El dia {dia_semana} es Lunes")
    case 2:
        print(f"El dia {dia_semana} es Martes")
    case 3:
        print(f"El dia {dia_semana} es Miércoles")
    case 4:
        print(f"El dia {dia_semana} es Jueves")
    case 5:
        print(f"El dia {dia_semana} es Viernes")
    case 6:
        print(f"El dia {dia_semana} es Sábado")
    case 7:
        print(f"El dia {dia_semana} es Domingo")

