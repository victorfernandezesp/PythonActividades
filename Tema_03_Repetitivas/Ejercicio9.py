""" Ejercicio 9.
        Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos
        mostrar.

    Author: Victor Fernandez España
    Curso:  2022-2023
"""
import math

print("Este programa te dice los N primeros numeros primos ")
n_primos = int(input("Cuantos primos quieres que muestre? "))
print(f"Los {n_primos} primeros primos: ")
contador_primos = 1
print(f"{contador_primos}º = 2")
posible_primo = 3

while contador_primos < n_primos:
    es_primo = True
    divisor = 3
    while divisor <= math.sqrt(posible_primo) and es_primo:
        if posible_primo % divisor == 0:
            es_primo = False
        divisor += 2
    if es_primo:
        contador_primos += 1
        print(f"{contador_primos}º = {posible_primo}")
    posible_primo += 2