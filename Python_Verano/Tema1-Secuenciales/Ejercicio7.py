# 7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde
# Author: Victor Fernandez España
#

# Introducimos por teclado el número con el que vamos a trabajar
minutos = int(input("Introduce el numero de minutos "))

# Realizamos las distintas operaciones
horas = int(minutos / 60)
minutos_fin = int(minutos % 60)

# Mostramos por pantalla los resultados
print(" Corresponde a: \n ", horas, "horas y ", minutos_fin, "minutos")