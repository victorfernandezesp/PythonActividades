""" Ejercicio 23.2.
        Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen,
        proporcione la calificación cualitativa correspondiente al número dado. La calificación cualitativa será
        una de las siguientes: «Suspenso» (nota menor que 5), «Aprobado» (nota mayor o igual que 5, pero menor que 7),
        «Notable» (nota mayor o igual que 7, pero menor que 9), «Sobresaliente» (nota mayor o igual que 9, pero menor
        que 10), «Matrícula de Honor» (nota 10).
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
import sys

ERROR_NOTA_NO_NUMERO = 2

ERROR_DESBORDAMIENTO_NOTA = 1
print("Este programa te dice cual es tu calificación ")
nota = float(input("Introduce la calificación que sacaste (1-10), por favor! "))
nota = round(nota)

if 1 > nota or nota > 10:
    print(f"ERROR. Tiene que ser un numero entre 1 y 10 ", file=sys.stderr)
    sys.exit(ERROR_DESBORDAMIENTO_NOTA)

match nota:
    case 1 | 2 | 3 | 4:
        print("Suspenso")
    case 5 | 6:
        print("Aprobado")
    case 7 | 8:
        print("Notable")
    case 9:
        print("Sobresaliente")
    case 10:
        print("Matricula de Honor")
