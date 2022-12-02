""" 5.  Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en
        cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.


    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("Este programa te dice que persona es mayor de entre 2 ")
persona1 = int(input("Introduce la edad de la persona numero 1, por favor! "))
persona2 = int(input("Introduce la edad de la persona numero 1, por favor! "))


if persona1 > persona2:
    print(f"La persona 1 con edad ({persona1}) es mayor que la persona 2 con edad ({persona2}) ")

elif persona1 < persona2:
    print(f"La persona 2 con edad ({persona2}) es mayor que la persona 1 con edad ({persona1}) ")

else:
    print(f"Ambos tienen la misma edad")
