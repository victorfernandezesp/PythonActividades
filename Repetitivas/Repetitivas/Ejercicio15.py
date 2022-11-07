""" Ejercicio 15.
        Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee
        igual adelante que atrás.



    Author: Victor Fernandez España
    Curso:  2022-2023
"""
print("Este programa te dice si es palíndromo o no")
cadena = input("Introduce la cadena: ")
cadena = cadena.lower()
cadena_rev = ""

for i in cadena:
    cadena_rev = i + cadena_rev

if cadena == cadena_rev:
    print("Es una cadena palíndroma ")
else:
    print("NO es una cadena palíndroma ")
