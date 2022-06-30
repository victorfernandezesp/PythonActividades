# 18. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

# Author: Victor Fernandez España


# Introducimos por teclado el número con el que vamos a trabajar
nombre = input("Escribe tu nombre: ")
apellido1 = input("Escribe tu primer apellido: ")
apellido2 = input("Escribe tu segundo apellido: ")


# Realizamos las distintas operaciones
nombre = nombre[0]
apellido1 = apellido1[0]
apellido2 = apellido2[0]

iniciales = nombre+apellido1+apellido2

# Mostramos por pantalla los resultados

print(f"Las iniciales son {iniciales}")