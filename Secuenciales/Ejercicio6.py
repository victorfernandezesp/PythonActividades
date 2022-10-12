""" 6. Calcular la media de tres números pedidos por teclado.
       Este programa mediante una entrada por teclado almacena 3 números en 3 variables, y luego realiza una
       serie de cálculos (media) y mediante un mensaje lo muestra por pantalla el resultado de la media.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("¡Introduce los 3 números y te haré la media ")
numero1 = float(input("¡Introduce el valor del numero 1, por favor! "))
numero2 = float(input("¡Introduce el valor del numero 2, por favor! "))
numero3 = float(input("¡Introduce el valor del numero 3, por favor! "))

media = (numero1 + numero2 + numero3)/3

print("El resultado de la media de los números ", numero1, ", ", numero2, "y ", numero3, " es = ", media)