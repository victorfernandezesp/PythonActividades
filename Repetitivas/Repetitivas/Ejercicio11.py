""" Ejercicio 11.

    Author: Victor Fernandez España
    Curso:  2022-2023
"""

print("Este programa te dice cuantas palabras hay en una cadena ")
cadena = input("Escriba la cadena: ")
espacio = " "
palabras = 1
for i in cadena:
    if i == espacio:
        palabras += 1
print(f"Hay {palabras} palabra/as")
