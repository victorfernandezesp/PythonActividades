""" 3. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
       Este programa mediante una entrada por teclado almacena en 2 variables, cateto 1 y cateto 2 luego calcula la
       hipotenusa y mediante un mensaje lo muestra por pantalla.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("¡Introduce cuanto valen los catetos y te calculare la hipotenusa! ")
cateto1 = float(input("¡Introduce el valor del cateto numero 1, por favor! "))
cateto2 = float(input("¡Introduce el valor del cateto numero 2, por favor! "))

hipotenusa = round((cateto1 ** 2 + cateto2 ** 2) ** 0.5, 2)

print("La hipotenusa del triangulo es ", hipotenusa)
