"""
    Ejercicio 7:

        Se desea almacenar las calificaciones del alumnado de 1DAW del IES Gran Capitán en los módulos de PROGRAMACIÓN,
        LENGUAJE DE MARCAS, BASES DE DATOS Y SISTEMAS INFORMÁTICOS.

        El número de alumnos no lo sabemos de antemano por lo que se han de añadir conforme se vayan introduciendo los
        datos.

        El programa pedirá el nombre y apellidos del alumno y a continuación las calificaciones en los módulos
        mencionados anteriormente.

        Cuando el usuario desee dejar de introducir información deberá de introducir una cadena vacía al introducir
        el nombre.

        Asimismo el programa deberá de proporcionar las siguientes funcionalidades:

        Impresión de las calificaciones del curso completo.
        Impresión de las calificaciones de un alumno en concreto. El programa pedirá nombre y apellidos del alumno y de
        encontrarlo mostrará las calificaciones de todos los módulos de este alumno.
        Nota media de un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota
        media.
        Nota máxima en un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota
        máxima así como el alumno con la misma.
        Nota más baja en un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota
        más baja así como el alumno con la misma.
        Listado ordenado de los datos con respecto a su nota (de mayor a menor). El programa pedirá el módulo y deberá
        de ser capaz de realizar una ordenación descendente por dicha nota.
        Nota: En las listas de python se pueden mezclar datos de diferente tipo. Aprovecha los módulos y funciones de
        python que faciliten las operaciones que se piden.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import random

asignaturas = ["PG", "LM", "BD", "SI"]
nombre_apellidos = []
num_alumnos = 0
while True:
    nombre = input("Escribe el nombre del alumno:   ")
    if nombre == "":
        break
    else:
        apellidos = input("Escribe el apellido del alumno:  ")
        num_alumnos += 1
        print(f"Has almacenado {num_alumnos} alumno/os")
        cadena_completa = nombre[1:7] + " " + apellidos[1:4]
        nombre_apellidos.append(cadena_completa)

FILAS = num_alumnos
COLUMNAS = len(asignaturas)
print("            ", "| PG |  LM |  BD |  SI |")
matriz = [[0] * COLUMNAS for _ in range(FILAS)]
for x in range(FILAS):
    print(f"{nombre_apellidos[x]:3}   ", end="")
    for y in range(COLUMNAS):
        numero = (random.random() * 11, 3)
        matriz[x][y] = 
        print(f"{matriz[x][y]:3d}   ", end="")
    print(" ")