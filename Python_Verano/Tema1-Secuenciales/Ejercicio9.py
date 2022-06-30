# 9.Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar
# finalmente por su compra.
# Author: Victor Fernandez España
#

# Introducimos por teclado el número con el que vamos a trabajar
compra = float(input("Introduce el coste de la compra "))

# Realizamos las distintas operaciones
descuento = round((compra*0.15), 2)
precio_final = round((compra-descuento), 2)

# Mostramos por pantalla los resultados
print(" El descuento es de : ", descuento, " € y el costo final es", precio_final, "€")
