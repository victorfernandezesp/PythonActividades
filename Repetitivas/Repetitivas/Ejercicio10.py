""" Ejercicio 10.
        Pide una cadena y un caracter por teclado y muestra cuantas veces aparece el caracter en la cadena.

    Author: Victor Fernandez España
    Curso:  2022-2023
"""

print("Este programa te dice cuantas veces aparece un caracter en una cadena ")
cadena = input("Escriba la cadena: ")
caracter = input("Escribe el caracter a buscar: ")
veces_caracter = 0
for i in cadena:
    if i == caracter:
        veces_caracter += 1
print(f"Aparece {veces_caracter} veces")
