# 2.Calcular el perímetro y área de un rectángulo dada su base y su altura.
# Author: Victor Fernandez España
# En este ejercicio recibimos por teclado la base y la altura en formato float por si salen decimales, calculamos el
# perimetro y el area y la mostramos por pantalla

# Guardamos en las variables los valores de entrada
base = float(input("Introduce la base "))
altura = float(input("Introduce la altura "))

# Se calcula el perimetro y el area
perimetro = (base*2) + (altura*2)
area = base * altura

# Se imprime los resultados
print("El perimetro es ", perimetro, " y el area ", area, ".")