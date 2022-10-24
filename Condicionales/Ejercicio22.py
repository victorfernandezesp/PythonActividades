""" Ejercicio 22.
        Realiza un programa que pida cinco números enteros y diga cuál es el mayor.

    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("Este programa te dice cual de los 3 números es mayor ")
numero1 = int(input("Dime el numero A, por favor! "))
numero2 = int(input("Dime el numero B, por favor! "))
numero3 = int(input("Dime el numero C, por favor! "))
numero4 = int(input("Dime el numero D, por favor! "))
numero5 = int(input("Dime el numero E, por favor! "))


if numero1 > numero2 and numero1 > numero3 and numero1 > numero4 and numero1 > numero5:
    print(f"El numero {numero1} es el mayor")

elif numero2 > numero1 and numero2 > numero3 and numero2 > numero4 and numero2 > numero5:
    print(f"El numero {numero2} es el mayor")

elif numero3 > numero1 and numero3 > numero2 and numero3 > numero4 and numero3 > numero5:
    print(f"El numero {numero3} es el mayor")

elif numero4 > numero1 and numero4 > numero2 and numero4 > numero3 and numero4 > numero5:
    print(f"El numero {numero4} es el mayor")

elif numero5 > numero1 and numero5 > numero2 and numero5 > numero3 and numero5 > numero4:
    print(f"El numero {numero5} es el mayor")

else:
    print(f"Has introducido 2 o mas números iguales, no hay ninguno mayor")
