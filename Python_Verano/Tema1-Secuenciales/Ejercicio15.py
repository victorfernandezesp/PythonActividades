# 15. Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie
# los valores de ambas variables y muestre cuanto valen al final las dos variables.
# Author: Victor Fernandez España


# Introducimos por teclado el número con el que vamos a trabajar

var_A = int(input("Introduce un numero para almacenar en la variable A "))
var_B = int(input("Introduce un numero para almacenar en la variable B "))

# Realizamos las distintas operaciones
aux1 = var_A
var_A = var_B
var_B = aux1

# Mostramos por pantalla los resultados
print(f" La variable A ahora vale {var_A} y la variable B vale {var_B}")