""" 4.  Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de
        aviso en caso contrario.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("Este programa te devuelve el resultado de una division ")
num1 = int(input("Introduce el numero 1, por favor! "))
num2 = int(input("Introduce el numero 2, por favor! "))

if num2 != 0:
    div = num1 / num2
    print(f"El resultado de dividir {num1}/{num2} es {div} ")

else:
    print(f"El numero 2 es {0} y no se puede dividir por 0!!!")
