""" 7.  Realiza un programa que calcule la potencia, para ello pide por teclado la base y el exponente.
        Pueden ocurrir tres cosas:

            El exponente sea positivo, sólo tienes que imprimir la potencia.
            El exponente sea 0, el resultado es 1.
            El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

    Author: Victor Fernandez España
    Curso:  2022-2003
"""
import math
print("Este programa calcula la potencia ")
base = int(input("Introduce la base, por favor! "))
exponente = int(input("Introduce el exponente, por favor! "))

if exponente == 0:
    print(f"El resultado de la potencia es 1.")
elif exponente < 0:
    print(f"El resultado de la potencia es {1/math.pow(base,-exponente)}.")

else:
    print(f"El resultado de la potencia es {math.pow(base,exponente)}.")
