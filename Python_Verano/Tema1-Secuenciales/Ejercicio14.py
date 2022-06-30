# 14. Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
# Author: Victor Fernandez España
#

# Introducimos por teclado el número con el que vamos a trabajar

number1 = int(input("Introduce un numero de 2 cifras "))

# Realizamos las distintas operaciones
aux1 = int(number1 % 10)*10
aux2 = int(number1 / 10)
resultado = int(aux1 + aux2)

# Mostramos por pantalla los resultados
print(f" El numero invertido es: {resultado} ")