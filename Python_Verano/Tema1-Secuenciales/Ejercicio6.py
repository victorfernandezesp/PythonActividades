# 6. Calcular la media de tres números pedidos por teclado.
# Author: Victor Fernandez España
# En este programa se introducirá 3 valores por teclado cuyo
# resultado sera la media aritmética y se mostrara por pantalla

# Introducimos por teclado los dos números con los cuales vamos a trabajar
numero1 = float(input("Introduce el primero numero "))
numero2 = float(input("Introduce el segundo numero "))
numero3 = float(input("Introduce el tercer numero "))

# Realizamos las distintas operaciones
media = (numero1 + numero2 + numero3)/3

# Mostramos por pantalla los resultados
print("La media de los 3 numero es ", media)