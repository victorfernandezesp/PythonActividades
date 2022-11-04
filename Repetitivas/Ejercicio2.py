""" Ejercicio 2.
        Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
        El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

    Author: Victor Fernandez España
    Curso:  2022-2023
"""
print("Este programa cuenta los numeros mayores a 0, menores a 0 e iguales a 0 ")
numeros_usuario = int(input("Introduce cuantos numeros quieres que clasifique "))
mayores_0 = 0
menores_0 = 0
iguales_0 = 0

for i in range(0, numeros_usuario):
    numero_clasificar = int(input("Introduce un numero para clasificarlo "))
    if numero_clasificar > 0:
        mayores_0 += 1
    elif numero_clasificar == 0:
        iguales_0 += 1
    else:
        menores_0 += 1
print(f"Hay {mayores_0} mayores que 0")
print(f"Hay {iguales_0} iguales a 0")
print(f"Hay {menores_0} menores que 0")