""" 9.Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar
      finalmente por su compra.

       Este programa mediante una entrada por teclado de compras que realiza y que almacena en una variable, realizara
       una serie de cálculos para adivinar el descuento y mediante un mensaje lo muestra por pantalla el resultado en
       euros.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("¡Introduce el costo de la compra en euros ")
compra = float(input("¡Introduce el costo de tu compra, por favor! "))

descuento = compra * 0.15
compra_desc = compra - descuento

print(" El descuento es de ", descuento, " €, la compra después de la rebaja sale a ", compra_desc, " €.")