""" 8. Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto
        dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en
        el mes tomando en cuenta su sueldo base y comisiones.
       Este programa mediante una entrada por teclado de ventas que realiza y que almacena en una variable, realizara
       una serie de cálculos para adivinar la comisión y mediante un mensaje lo muestra por pantalla el resultado en
       euros.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("¡Introduce el sueldo base del trabajador, el costo de las 3 ventas y te dire cuanto recibirá por comisión y en "
      "total ")
sueldo_base = float(input("¡Introduce tu sueldo base, por favor! "))
venta1 = float(input("¡Introduce el valor de tu venta 1, por favor! "))
venta2 = float(input("¡Introduce el valor de tu venta 2, por favor! "))
venta3 = float(input("¡Introduce el valor de tu venta 3, por favor! "))

comisiones = (venta1 + venta2 + venta3) * 0.1
sueldo_total = sueldo_base + comisiones

print("El resultado total de las comisiones es ", comisiones, " euros, y el sueldo total con comisiones es de",
      sueldo_total, " euros ")