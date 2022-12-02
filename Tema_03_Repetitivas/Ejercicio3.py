""" Ejercicio 3.
       Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa
       termina cuando se introduce un espacio.
    Author: Victor Fernandez España
    Curso:  2022-2023
"""
import sys

VOCALES = "aeoiuáéóíúàèòìùâêôîûü"

ERROR_LONGITUD_O_LETRA = 1
print("Este programa te dice si los caracteres introducidos son vocales o no, finaliza cuando introduces un espacio ")
while True:
    char = input("Introduce el caracter y te dire si es vocal o no, por favor ")
    char.lower()
    if len(char) != 1 or not char.isalpha():
        print(f"ERROR. tienes que introducir un solo caracter y tiene que ser una letra ", file=sys.stderr)
        sys.exit(ERROR_LONGITUD_O_LETRA)
    if char in VOCALES:
        print("VOCAL")
    else:
        print("NO VOCAL")
    if char == " ":
        print("¿Hasta la próxima!")
        break