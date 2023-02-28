"""
    Ejercicio 8:
        Muestra un menú con las siguientes opciones:

        - Introducir (por teclado) una fecha pidiendo por teclado año, mes y día en formato dd/mm/aaaa. Si no se
            introduce correctamente se devuelve un mensaje de error. Usa una función booleana para validar la fecha.

        - Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su
            valor. Si el número es negativo restará los días. Esta opción solo podrá realizarse si hay una fecha
            introducida (se ha ejecutado la opción anterior), si no la hay mostrará un mensaje de error.

        - Añadir meses a la fecha. El mismo procedimiento que la opción anterior.

        - Añadir años a la fecha. El mismo procedimiento que la opción 2.

        - Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa (válida, si no lo es
            da error) y la comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior,
            igual o posterior a la que tenemos almacenada y el número de días comprendido entre las dos fechas.

        - Mostrar la fecha en formato largo (ejemplo: "lunes, 1 de febrero de 2021").

        - Terminar.

        Consideraciones a tener en cuenta:

        El menú lo hacemos con una clase a la que llamaremos Menú, esa clase permitirá ir añadiendo opciones y escoger
        alguna opción.
        Las fechas las manejaremos con la clase datetime. Date.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import datetime
from dateutil.relativedelta import relativedelta
import locale
import sys

from Tema_06_POO.Tanda2POO.ejercicio8.menu import Menu

SALIDA_DEL_PROGRAMA_CON_EXITO = 0

menu1 = Menu("MANEJA FECHAS",
             "Introducir fecha.",
             "Añadir días a la fecha.",
             "Añadir meses a la fecha.",
             "Añadir años a la fecha.",
             "Comparar la fecha.",
             "Mostrar la fecha en formato largo.")

fecha_introducida = False


def imprimir_fecha():
    locale.setlocale(locale.LC_ALL, 'es-ES')
    fecha_formato_largo = fecha1.strftime('%A %d %B %Y')
    print(fecha_formato_largo)


while True:
    option = menu1.escoger()
    match option:

        case 1:
            fecha = input("Introduce una fecha en formato dd/mm/aaaa:   ")
            dia = fecha[:2]
            mes = fecha[3:5]
            ano = fecha[6:]
            if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
                print("Debes introducir una fecha en formato dd/mm/aaaa.")
                continue
            else:
                fecha1 = datetime.date(int(ano), int(mes), int(dia))
                fecha_introducida = True

        case 2:
            if not fecha_introducida:
                print("Primero debes introducir una fecha.")
                continue
            numero_de_dias_a_sumar = int(input("¿Cuántos días quieres sumar a la fecha?:    "))
            if numero_de_dias_a_sumar < 0:
                numero_de_dias_a_sumar = abs(numero_de_dias_a_sumar)
                fecha1 -= relativedelta(days=numero_de_dias_a_sumar)
            else:
                fecha1 += relativedelta(days=numero_de_dias_a_sumar)

            imprimir_fecha()

        case 3:
            if not fecha_introducida:
                print("Primero debes introducir una fecha.")
                continue
            numero_de_meses_a_sumar = int(input("¿Cuántos meses quieres sumar a la fecha?:    "))
            if numero_de_meses_a_sumar < 0:
                fecha1 -= relativedelta(months=numero_de_meses_a_sumar)
            else:
                fecha1 += relativedelta(months=numero_de_meses_a_sumar)

            imprimir_fecha()

        case 4:
            if not fecha_introducida:
                print("Primero debes introducir una fecha.")
                continue

            numero_de_anos_a_sumar = int(input("¿Cuántos años quieres sumar a la fecha?:    "))
            if numero_de_anos_a_sumar < 0:
                fecha1 -= relativedelta(year=numero_de_anos_a_sumar)

            else:
                fecha1 += relativedelta(year=numero_de_anos_a_sumar)

            imprimir_fecha()

        case 5:
            if not fecha_introducida:
                print("Primero debes introducir una fecha.")
                continue
            fecha = input("Introduce otra fecha en formato dd/mm/aaaa:   ")
            dia = fecha[:2]
            mes = fecha[3:5]
            ano = fecha[6:]
            if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
                print("Debes introducir una fecha en formato dd/mm/aaaa.")
                continue
            else:
                fecha2 = datetime.date(int(ano), int(mes), int(dia))

            if fecha1 > fecha2:
                print("La fecha 2 es mas antigua que la fecha 1")

            elif fecha1 < fecha2:
                print("La fecha 1 es mas antigua que la fecha 2")

            else:
                print("Las fechas son iguales")

        case 6:
            if not fecha_introducida:
                print("Primero debes introducir una fecha.")
                continue
            imprimir_fecha()

        case 7:
            sys.exit(SALIDA_DEL_PROGRAMA_CON_EXITO)
