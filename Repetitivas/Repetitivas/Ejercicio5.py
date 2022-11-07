""" Ejercicio 5.
        Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que
        el superior lo tiene que volver a pedir.

        A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las
        siguientes informaciones:

        La suma de los números que están dentro del intervalo (intervalo abierto).
        Cuantos números están fuera del intervalo.
        Informa si hemos introducido algún número igual a los límites del intervalo.

    Author: Victor Fernandez España
    Curso:  2022-2023
"""

print("Este programa te cuenta los numeros dentro, fuera y coincidentes con el intervalo ")
num_fuera = 0
num_intervalo = 0
num_dentro = 0
limite_inferior = int(input("Introduce el limite_inferior, por favor "))
limite_superior = int(input("Introduce el limite_superior, por favor "))

while limite_inferior >= limite_superior:
    print("El limite inferior tiene que ser inferior al limite superior, vuelve a introducirlo, por favor. ")
    limite_inferior = int(input("Introduce el limite_inferior, por favor "))
    limite_superior = int(input("Introduce el limite_superior, por favor "))


while True:
    num_introducir = int(input("Introduce numero, por favor "))
    if num_introducir == 0:
        break
    if num_introducir < limite_inferior:
        num_fuera += 1
    elif num_introducir == limite_inferior or num_introducir == limite_superior:
        num_intervalo += 1
    else:
        num_dentro += num_introducir

print(f"Hay {num_fuera} numeros fuera del intervalo")
print(f"La suma de los numero dentro del intervalo es {num_dentro}")
print(f"Hay {num_intervalo} numeros iguales a los limites")