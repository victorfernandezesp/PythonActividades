""" 15. Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie
        los valores de ambas variables y muestre cuanto valen al final las dos variables.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("Este programa te intercambia los números de 2 variables")
numeroA = int(input("¡Introduce el numero A, por favor! "))
numeroB = int(input("¡Introduce el numero B, por favor! "))

auxiliar = numeroA
numeroA = numeroB
numeroB = auxiliar

print("El valor de la variable A, ahora, es ", numeroA, " y el valor de la variable B es ", numeroB)