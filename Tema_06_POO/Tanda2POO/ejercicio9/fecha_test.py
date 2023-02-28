"""
    Ejercicio 9:
       Nos hemos enterado de que la clase datetime. Date ha sido comprometida y tenemos que crear una clase nueva para
       almacenar fechas locales (Date), en este caso la clase será mutable (los objetos pueden cambiar el día, mes o
       año). Los objetos de la clase Fecha son fechas de tiempo y se crean de la forma:

        f1 = Date(1, 10, 2020)  # almacena el 1 de octubre de 2020
        f2 = Date(f1)  # almacena una copia de la fecha almacenada en f1

        Para simplificar consideraremos que las fechas son todas a partir del 1 de enero del año 1.

        Si al constructor se le pasan valores incorrectos lanzaremos la excepción ValueError.

        Crea métodos para:

        - Sumar y restar días a la fecha.

        - Restar fechas. Devuelve el número de días comprendidos entre ambas.

        - Comparar la fecha almacenada con otra.

        - Saber si el año de la fecha almacenada es bisiesto.

        - Obtener el día de la semana de una fecha concreta.

        - El método __str__() devuelve una cadena con el formato "<día del mes> de <nombre del mes> de <año>".


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

from Tema_06_POO.Tanda2POO.ejercicio9.fecha import Fecha

fecha1 = Fecha(15, 11, 2003)
print(fecha1)
fecha1.obtener_dia_semana()

