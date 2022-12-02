""" Ejercicio 12.
        Escribir un programa que lea un año indicar si es bisiesto.

        Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también
        sea divisible por 400.

    Author: Victor Fernandez España
    Curso:  2022-2003
"""

print("Este programa te dice si el año introducido por teclado es bisiesto o no ")
ano = int(input("Introduce el año, por favor! "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"{ano} es un año bisiesto ")
else:
    print(f"{ano} no es un año bisiesto ")
