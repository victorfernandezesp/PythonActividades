""" 4. Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
       Este programa mediante una entrada por teclado almacena en 2 variables, numero 1 y numero 2 luego realiza una
       serie de cálculos y mediante un mensaje lo muestra por pantalla.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("¡Introduce cuanto valen los números y te calculare la suma, resta, multiplicacion y division de ambos! ")
numero1 = float(input("¡Introduce el valor del numero 1, por favor! "))
numero2 = float(input("¡Introduce el valor del numero 2, por favor! "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 - numero2
division = numero1 / numero2

print("El resultado de sumar ", numero1, " y ", numero2, " es = ", suma)
print("El resultado de restar ", numero1, " y ", numero2, " es = ", resta)
print("El resultado de multiplicar ", numero1, " y ", numero2, " es = ", multiplicacion)
print("El resultado de dividir ", numero1, " y ", numero2, " es = ", division)