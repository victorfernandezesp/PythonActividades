""" Ejercicio 23.1.
        Diseña un programa que, dados cinco números enteros, determine cuál de los cuatro últimos números es más cercano
        al primero. Por ejemplo, si el usuario introduce los números 2, 6, 4, 1 y 10, el programa responderá que el
        número más cercano al 2 es el 1.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("Este programa te dice cual de los 4 últimos números es mas cercano al siguiente ")
numero1 = int(input("Dime el numero A, por favor! "))
numero2 = int(input("Dime el numero B, por favor! "))
numero3 = int(input("Dime el numero C, por favor! "))
numero4 = int(input("Dime el numero D, por favor! "))
numero5 = int(input("Dime el numero E, por favor! "))


candidato = numero2
distancia = abs(numero1 - numero2)

if abs(numero1-numero3) < distancia:
    candidato = numero3
    distancia = abs(numero1 - numero3)

if abs(numero1-numero4) < distancia:
    candidato = numero4
    distancia = abs(numero1 - numero4)

if abs(numero1-numero5) < distancia:
    candidato = numero5
print(f"El número con menor distancia a {numero1} es el numero {candidato}.")
