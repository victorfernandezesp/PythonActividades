# 7. Programa que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es
# mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero
# el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.
# Author: Victor Fernandez España

# Introducimos por teclado el número con el que vamos a trabajar
nota = int(input("Introduce una nota por teclado: "))
edad = int(input("Introduce una edad por teclado: "))
sex = str(input("Introduce tu caracter de sexo, F si eres mujer y M si es Hombre "))
print(f"-----------------------------------------------------------------")

# Realizamos las distintas operaciones
if nota >= 5 and edad >= 18 and sex.upper() == 'F':
    print(f"ACEPTADA")

elif nota >= 5 and edad >= 18 and sex.upper() == 'M':
    print(f"POSIBLE")
else:
    print(f"NO ACEPTADA")