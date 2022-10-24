""" Ejercicio 11.
        Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
        El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

        Si se cumple Pitágoras entonces es triángulo rectángulo
        Si sólo dos lados del triángulo son iguales entonces es isósceles.
        Si los 3 lados son iguales entonces es equilátero.
        Si no se cumple ninguna de las condiciones anteriores, es escaleno.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
from math import pow
print("Este programa te dice según sus lados que tipo de triangulo que es")
lado_mas_largo = float(input("Introduce el lado del triangulo mas largo, si existe, por favor! "))
lado2 = float(input("Introduce el lado 2 del triangulo, por favor! "))
lado3 = float(input("Introduce el lado 3 del triangulo, por favor! "))


if lado_mas_largo == lado2 == lado3:
    print(f"Es un triangulo equilátero ")

elif pow(lado_mas_largo, 2) == pow(lado2, 2) + pow(lado3, 2):
    print(f"Es un triangulo rectángulo ")

elif lado2 == lado3 or lado3 == lado_mas_largo or lado2 == lado_mas_largo:
    print(f"Es un triangulo isósceles")

else:
    print(f"Es un triangulo escaleno")
