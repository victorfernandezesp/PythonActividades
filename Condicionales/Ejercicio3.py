""" 3. Escribe un programa que lea un número e indique si es par o impar.

    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("Este programa te dice si el numero es par o impar ")
num1 = int(input("Introduce el numero, por favor! "))

if num1 % 2 == 0:
    print(f"El numero ({num1}) es par")

else:
    print(f"El numero ({num1}) es impar")
