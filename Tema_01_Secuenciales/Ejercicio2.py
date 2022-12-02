""" 2. Calcular el perímetro y área de un rectángulo dada su base y su altura.
       Este programa mediante una entrada por teclado almacena en 2 variables, base y altura, luego calcula el perimetro
       y area y mediante un mensaje lo muestra por pantalla
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("Este programa calcula el area y el perimetro de un rectángulo dada su base y altura")
base = float(input("Introduzca la base del rectángulo "))
altura = float(input("Introduzca la altura del rectángulo "))

perimetro = base * 2 + altura * 2
area = base * altura

print("El perimetro es ", perimetro, " y el area ", area, ".")
