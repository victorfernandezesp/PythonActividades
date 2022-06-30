# 8. Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto
# dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes
# tomando en cuenta su sueldo base y comisiones.
# Author: Victor Fernandez España
#

# Introducimos por teclado el número con el que vamos a trabajar
sueldo_base = float(input("Introduce el sueldo base "))
venta1 = float(input("Introduce el valor de la venta 1 "))
venta2 = float(input("Introduce el valor de la venta 2 "))
venta3 = float(input("Introduce el valor de la venta 3 "))

# Realizamos las distintas operaciones
comisiones = round(((venta1 + venta2 + venta3) * 0.1), 2)
sueldo_final = round((comisiones + sueldo_base), 2)

# Mostramos por pantalla los resultados
print(" El valor de las comisiones de venta son : ", comisiones, " € y el sueldo final es", sueldo_final, "€")