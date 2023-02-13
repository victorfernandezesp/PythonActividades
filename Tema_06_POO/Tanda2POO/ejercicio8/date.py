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
from Tema_06_POO.Tanda2POO.ejercicio8.menu import Menu
from typeguard import typechecked


@typechecked
class Date:
    def __init__(self):
        pass
