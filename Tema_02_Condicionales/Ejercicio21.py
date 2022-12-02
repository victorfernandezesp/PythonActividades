""" Ejercicio 21.
        Realiza un programa que pida tres números enteros y diga cuál es el mayor.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("Este programa te dice cual de los 3 números es mayor ")
numero1 = int(input("Dime el numero A, por favor! "))
numero2 = int(input("Dime el numero B, por favor! "))
numero3 = int(input("Dime el numero C, por favor! "))

if numero1 > numero2 and numero1 > numero3:
    print(f"El numero {numero1} es el mayor")

elif numero2 > numero1 and numero2 > numero3:
    print(f"El numero {numero2} es el mayor")

elif numero3 > numero1 and numero3 > numero2:
    print(f"El numero {numero3} es el mayor")
else:
    print(f"Has introducido 2 o mas números iguales, no hay ninguno mayor")
