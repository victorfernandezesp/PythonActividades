# 14. Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
# Author: Victor Fernandez España


# En esta version se trata al numero como cadena y no como numero como tal de ahi que podamos coger del numero la
# posicion y seleccionar el caracter que en este caso es un numero, en la version 1 trabajamos con numeros y en la
# version 2 trabajamos con cadenas

# Introducimos por teclado el número con el que vamos a trabajar

number1 = input("Introduce un numero de 2 cifras ")

# Realizamos las distintas operaciones
aux1 = number1[1]
aux2 = number1[0]
resultado = number1[1] + number1[0]

# Mostramos por pantalla los resultados
print(f" El numero invertido es: {resultado} ")