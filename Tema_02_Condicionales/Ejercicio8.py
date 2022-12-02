""" Ejercicio 8.
    Programa que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’
    si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla
    lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar
    ‘NO ACEPTADA’.

    Author: Victor Fernandez España
    Curso:  2022-2003
"""
LONGITUD_MAXIMA_CHAR = 1
EDAD_MINIMA = 18
NOTA_MINIMA = 5
print("Este programa te muestra Aceptada, Posible, o No aceptado, dependiendo de su edad, nota y sexo ")
nota = float(input("Introduce tu nota, por favor! "))
edad = int(input("Introduce tu edad, por favor! "))
sexo = str(input("Introduce F si eres chica o M si eres chico, por favor! "))

if nota >= NOTA_MINIMA and edad >= EDAD_MINIMA and sexo == 'F':
    print(f"ACEPTADA")

elif nota >= NOTA_MINIMA and edad >= EDAD_MINIMA and sexo == 'M':
    print(f"POSIBLE")

else:
    print(f" NO ACEPTADO")