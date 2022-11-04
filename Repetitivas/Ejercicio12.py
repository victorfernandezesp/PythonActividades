""" Ejercicio 12.
        Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer
        carácter en la cadena por el segundo carácter.

    Author: Victor Fernandez España
    Curso:  2022-2023
"""
import sys

LONGITUD_CARACTER_MAYOR_A_1 = 1

print("Este programa substituye un caracter de la cadena introducida ")
cadena = input("Escriba la cadena: ")
caracter_a_subs = input("Escribe el caracter a substituir: ")
if len(caracter_a_subs) > 1:
    print(f"ERROR. Tiene que tener longitud 1 ", file=sys.stderr)
    sys.exit(LONGITUD_CARACTER_MAYOR_A_1)
caracter_que_lo_subs = input("Escribe el caracter que lo substituye substituir: ")
if len(caracter_que_lo_subs) > 1:
    print(f"ERROR. Tiene que tener longitud 1 ", file=sys.stderr)
    sys.exit(LONGITUD_CARACTER_MAYOR_A_1)


for i in cadena:
    cadena = cadena.replace(caracter_a_subs, caracter_que_lo_subs)
print(f"{cadena}")
