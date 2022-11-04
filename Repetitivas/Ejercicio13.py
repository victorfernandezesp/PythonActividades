""" Ejercicio 13.
        Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.

    Author: Victor Fernandez España
    Curso:  2022-2023
"""
print("Este programa cambia las mayúsculas a minúsculas y viceversa")
cadena = input("Introduce la cadena: ")
cadena_auxiliar = ""
for i in cadena:
    if i.isupper():
        cadena_auxiliar += i.lower()
    else:
        cadena_auxiliar += i.upper()
print(f"{cadena_auxiliar}")
