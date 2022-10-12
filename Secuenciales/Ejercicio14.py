""" 14. Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.

       Este programa mediante una entrada por teclado de 1 número almacenado en 1 variable, realizara una serie de
       cálculos para invertir el numero.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("¡Introduce el número que se le pedirán a continuación ")
numero1 = int(input("¡Introduce numero que se invertirá a continuación, por favor! "))

auxiliar1 = numero1 / 10
auxiliar2 = (numero1 % 10) * 10
numero_invertido = int(auxiliar1 + auxiliar2)

print(" El numero invertido es igual a: ", numero_invertido)