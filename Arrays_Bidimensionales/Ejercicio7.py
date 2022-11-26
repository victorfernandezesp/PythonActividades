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
        Nota media de un módulo. Se pedirá al usuario el nombre del módulo tras lo cual el programa mostrará la nota
        media.
        Nota máxima en un módulo. Se pedirá al usuario el nombre del módulo tras lo cual el programa mostrará la nota
        máxima así como el alumno con la misma.
        Nota más baja en un módulo. Se pedirá al usuario el nombre del módulo tras lo cual el programa mostrará la nota
        más baja así como el alumno con la misma.
        Listado ordenado de los datos con respecto a su nota (de mayor a menor). El programa pedirá el módulo y deberá
        de ser capaz de realizar una ordenación descendente por dicha nota.
        Nota: En las listas de python se pueden mezclar datos de diferente tipo. Aprovecha los módulos y funciones de
        python que faciliten las operaciones que se piden.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys
from random import randrange
from time import sleep

SALIDA_CON_EXITO = 1

asignaturas = ["PG", "LM", "BD", "SI"]
nombre_apellidos = []
num_alumnos = 0
cadena_mas_larga = 0
candidato = 0
nota_mas_alta = 0
posicion_en_y = 0
nota_mas_baja = 10
while True:
    nombre = input("Escribe el nombre del alumno:   ")
    if nombre == "":
        break
    else:
        apellidos = input("Escribe los apellidos del alumno:  ")
        num_alumnos += 1
        print(f"Has almacenado {num_alumnos} alumno/os")
        cadena_completa = nombre + " " + apellidos
        if len(cadena_completa) > cadena_mas_larga:
            cadena_mas_larga = len(cadena_completa)
        nombre_apellidos.append(cadena_completa)

print("Menu de opciones:")
print("Selecciona una de las siguientes opciones:   ")
print('1. Imprimir calificaciones' + '\n'
                                     '2. Salir')
print('---------------------------------------------------------------------------------------------------------------')
opcion_1 = int(input("¿Que vas a selecionar?    "))
sleep(0.75)
if opcion_1 == 1:
    FILAS = num_alumnos
    COLUMNAS = len(asignaturas)
    print(" " * cadena_mas_larga, " | PG   | LM  |  BD  |  SI  |")

    matriz = [[0] * COLUMNAS for _ in range(FILAS)]
    for x in range(FILAS):
        if len(nombre_apellidos[x]) < cadena_mas_larga:
            espacios_faltan = cadena_mas_larga - len(nombre_apellidos[x])
            print(f"{nombre_apellidos[x]:2} ", " " * espacios_faltan, end="")
        else:
            print(f"{nombre_apellidos[x]:}", end="  ")
        for y in range(COLUMNAS):
            matriz[x][y] = randrange(0, 11)
            print(f" {matriz[x][y]:3d}   ", end="")
        print(" ")
else:
    print('Has salido del programa con éxito.', file=sys.stderr)
    sys.exit(SALIDA_CON_EXITO)

while True:
    print(" ")
    print(" ")
    print(" ")
    print("Menu de opciones:")
    sleep(0.5)
    print("Selecciona una de las siguientes opciones:   ")
    print('1. Imprimir calificaciones.')
    print('2. Imprimir calificaciones de un alumno concreto.')
    print('3. Imprimir nota media de un modulo.')
    print('4. Imprimir nota mas alta de un modulo junto al alumno.')
    print('5. Imprimir nota mas baja de un modulo junto al alumno.')
    print('6. Ordena de forma descendente las notas de un modulo.')
    print('7. Salir')
    print('-----------------------------------------------------------------------------------------------------------')
    opcion = int(input("¿Que vas a selecionar?    "))
    sleep(0.75)
    match opcion:
        case 1:
            print("Has elegido imprimir calificaciones:")
            sleep(1.75)
            FILAS = num_alumnos
            COLUMNAS = len(asignaturas)
            print(" " * cadena_mas_larga, " | PG   | LM  |  BD  |  SI  |")

            matriz = [[0] * COLUMNAS for _ in range(FILAS)]
            for x in range(FILAS):
                if len(nombre_apellidos[x]) < cadena_mas_larga:
                    espacios_faltan = cadena_mas_larga - len(nombre_apellidos[x])
                    print(f"{nombre_apellidos[x]:2} ", " " * espacios_faltan, end="")
                else:
                    print(f"{nombre_apellidos[x]:}", end="  ")
                for y in range(COLUMNAS):
                    matriz[x][y] = randrange(0, 11)
                    print(f" {matriz[x][y]:3d}   ", end="")
                print(" ")
        case 2:
            print("Has elegido imprimir calificaciones de un alumno concreto.")
            sleep(1.05)
            while True:
                busca_nombre = input("Indica nombre y apellidos del alumno: ")
                if busca_nombre in nombre_apellidos:
                    posicion_x_alumno = nombre_apellidos.index(busca_nombre)
                    print(" " * len(busca_nombre), "| PG | LM | BD | SI |")
                    print(f"{nombre_apellidos[posicion_x_alumno]:3} ", end="")
                    print(f"{matriz[posicion_x_alumno]:3d}   ")
                    break
                else:
                    print(f"El alumno {busca_nombre} no se encuentra en la base de datos, vuelva a intentarlo.")
                    continue

        case 3:
            print("Has elegido imprimir la media de un modulo concreto.")
            sleep(1.05)
            while True:
                print("¿De que modulo quieres saber la media?")
                print("Programación -> PG")
                print("Lenguajes de Marcas -> LM")
                print("Bases de Datos -> BD")
                print("Sistemas Informáticos -> SI")
                modulo = input("PG / LM / BD / SI     ")
                if modulo in asignaturas:
                    posicion_x_modulo = asignaturas.index(modulo)
                    media = 0
                    for x in range(FILAS):
                        media += (matriz[x][posicion_x_modulo])
                    media = round(media / FILAS, 2)
                    print(f"La media del modulo de {modulo} es: {media}")
                    break
                else:
                    print(f"El modulo {modulo} no se encuentra en la base de datos, vuelva a intentarlo.")
                    continue
        case 4:
            print("¿De que modulo quieres saber la nota mas alta y a quien corresponde?")
            print("Programación -> PG")
            print("Lenguajes de Marcas -> LM")
            print("Bases de Datos -> BD")
            print("Sistemas Informáticos -> SI")
            modulo = input("PG / LM / BD / SI     ")
            if modulo in asignaturas:
                posicion_x_modulo = asignaturas.index(modulo)
                for x in range(FILAS):
                    candidato = (matriz[x][posicion_x_modulo])
                    if nota_mas_alta <= candidato:
                        nota_mas_alta = candidato
                        posicion_en_y = x
                print(f"La nota mas alta del modulo {modulo} ha sido de {nota_mas_alta} que pertenece al alumno: "
                      f"{nombre_apellidos[posicion_en_y]}")
                break
            else:
                print(f"El modulo {modulo} no se encuentra en la base de datos, vuelva a intentarlo.")
                continue
        case 5:
            print("¿De que modulo quieres saber la nota mas baja y a quien corresponde?")
            print("Programación -> PG")
            print("Lenguajes de Marcas -> LM")
            print("Bases de Datos -> BD")
            print("Sistemas Informáticos -> SI")
            modulo = input("PG / LM / BD / SI     ")
            if modulo in asignaturas:
                posicion_x_modulo = asignaturas.index(modulo)
                for x in range(FILAS):
                    candidato = (matriz[x][posicion_x_modulo])
                    if nota_mas_baja >= candidato:
                        nota_mas_baja = candidato
                        posicion_en_y = x
                print(f"La nota mas alta del modulo {modulo} ha sido de {nota_mas_baja} que pertenece al alumno: "
                      f"{nombre_apellidos[posicion_en_y]}")
                break
            else:
                print(f"El modulo {modulo} no se encuentra en la base de datos, vuelva a intentarlo.")
                continue
        case 6:
            print("¿De que modulo quieres el listado ordenado de los datos con respecto a su nota (de mayor a menor)")
            print("Programación -> PG")
            print("Lenguajes de Marcas -> LM")
            print("Bases de Datos -> BD")
            print("Sistemas Informáticos -> SI")
            modulo = input("PG / LM / BD / SI     ")
            if modulo in asignaturas:
                posicion_x_modulo = asignaturas.index(modulo)
                for x in range(FILAS):
                    candidato = (matriz[x][posicion_x_modulo])
                break
            else:
                print(f"El modulo {modulo} no se encuentra en la base de datos, vuelva a intentarlo.")
                continue
        case 7:
            sleep(1.55)
            print('Has salido del programa con éxito.', file=sys.stderr)
            sys.exit(SALIDA_CON_EXITO)
        case _:
            print('La opcion no es correcta')
            continue