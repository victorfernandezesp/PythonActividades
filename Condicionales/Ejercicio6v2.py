""" 6.  Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

    Author: Victor Fernandez España
    Curso:  2022-2003
"""
import sys

LONGITUD_CADENA = 1
print("Este programa lee una letra y te dice si es mayúscula o no ")
char1 = input("Introduce la cadena, por favor! ")

if len(char1) != LONGITUD_CADENA:
    print(f"ERROR. La cadena {char1} no puede tener mas de 1 carácter", file=sys.stderr)
    sys.exit(1)
if not char1.isalpha():
    print(f"ERROR.{char1} no es una letra", file=sys.stderr)
    sys.exit(2)

if char1 == char1.upper():
    print(f"Su letra esta en mayúscula")

else:
    print(f"Su letra esta en minúscula")
