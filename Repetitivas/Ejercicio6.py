""" Ejercicio 6.
        Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla
        el resultado de la potencia. No se puede utilizar el operador de potencia ni la función.

    Author: Victor Fernandez España
    Curso:  2022-2023
"""

print("Este programa te hace una potencia sin funciones ni operador potencia ")
potencia = 1
contador = 1
base = float(input("Introduce la base, por favor "))
exponente = int(input("Introduce el exponente, por favor "))

while contador <= exponente:
    potencia = potencia * base
    contador += 1

print(f" La potencia es {potencia}")