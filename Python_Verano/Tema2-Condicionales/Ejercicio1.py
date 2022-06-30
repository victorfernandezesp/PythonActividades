# 1. Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

# Author: Victor Fernandez España


# Introducimos por teclado el número con el que vamos a trabajar
number1 = int(input("Introduce el primer numero y te dire si es mayor que el 2: "))
number2 = int(input("Introduce el segundo numero y te dire si es mayor que el 1: "))

print(f"-----------------------------------------------------------------")


# Realizamos las distintas operaciones
if number1 > number2:
    # Mostramos por pantalla los resultados
    print(f"El numero 1 es mayor que el 2")
elif number1 == number2:
    # Mostramos por pantalla los resultados
    print(f"Ambos números son iguales")
else:
    # Mostramos por pantalla los resultados
    print(f"El numero 2 es mayor que el 1")
