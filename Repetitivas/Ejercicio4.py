""" Ejercicio 4.
       Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

    Author: Victor Fernandez España
    Curso:  2022-2023
"""

print("Este programa te imprime todos los numeros pares entre 2 numeros que se pidan ")
num1 = int(input("Introduce el numero1, por favor "))
num2 = int(input("Introduce el numero2, por favor "))
auxiliar = 0

if num1 > num2:
    auxiliar = num1
    num1 = num2
    num2 = auxiliar
if num1 % 2 != 0:
    num1 += 1
if num1 == 0:
    num1 += 2
for i in range(num1, num2+1, 2):
    print(f"{i} ")