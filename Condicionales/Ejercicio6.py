""" 6.  Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

    Author: Victor Fernandez España
    Curso:  2022-2003
"""
LONGITUD_CADENA = 1
print("Este programa lee una letra y te dice si es mayúscula o no ")
char1 = input("Introduce la cadena, por favor! ")

if len(char1) == LONGITUD_CADENA and char1.isalpha():
    if char1 == char1.upper():
        print(f"Su letra esta en mayúscula")
    else:
        print(f"Su letra esta en minúscula")

else:
    print(f" La cadena contiene mas de 1 carácter o no es una cadena, por favor, introduce una sola letra. ")
