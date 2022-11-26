"""
    Ejercicio 2:

        Escribe un programa que lea 10 números por teclado y que luego los muestre en orden inverso, es decir, el
        primero que se introduce es el último en mostrarse y viceversa.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
a = []
print("Este programa lee 10 numeros por teclado y luego los muestra en orden inverso")
for i in range(10):
    num_introducido = int(input("Introduce un numero: "))
    a.append(num_introducido)

print("Al reves seria asi:")
for x in a[::-1]:
    print(f" {x}")