# 3. Escribe un programa que lea un número e indique si es par o impar.
# Author: Victor Fernandez España


# Introducimos por teclado el número con el que vamos a trabajar
number = int(input("Introduce el numero y te dire si es par o impar: "))
print(f"-----------------------------------------------------------------")


# Realizamos las distintas operaciones
if number % 2 == 0:
    # Mostramos por pantalla los resultados
    print(f"El numero es par ")

else:
    # Mostramos por pantalla los resultados
    print(f"El numero es impar ")
