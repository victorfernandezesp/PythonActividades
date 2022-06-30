# 4. Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de
# aviso en caso contrario.
# Author: Victor Fernandez España


# Introducimos por teclado el número con el que vamos a trabajar
number1 = int(input("Introduce el numero1 para poder divirlo: "))
number2 = int(input("Introduce el numero2 para poder divirlo: "))
print(f"-----------------------------------------------------------------")

# Realizamos las distintas operaciones
if number2 != 0:
    division = float(number1/number2)
    # Mostramos por pantalla los resultados
    print(f"El numero resultante es {division} ")

else:
    # Mostramos por pantalla los resultados
    print(f" No puedo dividir por 0! ")
