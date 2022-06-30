# 4.Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
# Author: Victor Fernandez España
# En este programa se introducirán 2 valores por teclado los cuales utilizaremos para realizar 4 operaciones cuyos
# resultados se mostraran por pantalla

# Introducimos por teclado los dos números con los cuales vamos a trabajar

numero1 = float(input("Introduce el primer numero "))
numero2 = float(input("Introduce el segundo numero "))

# Realizamos las distintas operaciones
suma = numero1 + numero2
resta = numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2

# Mostramos por pantalla los resultados

print("\n El resultado de la suma es ", suma, "\n El resultado de la resta es resta ", resta,
      "\n El resultado de la division es ", division, "\n El resultado de la multiplicación es ", multiplicacion)