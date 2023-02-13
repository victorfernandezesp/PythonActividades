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
import sys

from typeguard import typechecked

SALIDO_CON_EXITO = 0


@typechecked
class Menu:
    def __init__(self, titulo, *opciones):
        self.__titulo = titulo
        self.__opciones = list(opciones)
        self.__opciones.append("Terminar")

    @property
    def titulo(self):
        return self.__titulo

    @property
    def opciones(self):
        return self.__opciones

    def mostrar_opciones(self):
        contador = 1
        print(f"{self.__titulo}:")
        print("Selecciona una de las siguientes opciones:   ")
        for i in self.__opciones:
            print(f"{contador}. {i}")
            contador += 1
        print('-------------------------------------------------------------------------------------------------------')

    def escoger_opciones(self):
        self.mostrar_opciones()
        x = int(input("¿Que vas a seleccionar?    "))
        if x == len(self.__opciones):
            sys.exit(SALIDO_CON_EXITO)
        return x

    def anadir_opciones(self):
        nueva_opcion = input("¿Cuál es la opción nueva a añadir?")
        pregunta_si_anade_al_final = input("¿Desea añadirlo como ultima opción? (S/N)")
        pregunta_si_anade_al_final.upper()
        if pregunta_si_anade_al_final == "S":
            self.__opciones.insert(len(self.__opciones) - 1, nueva_opcion)
        else:
            while True:
                pregunta_posicion = int(input("¿En que posicion desea añadirlo?"))
                if len(self.__opciones) > pregunta_posicion > -1:
                    self.__opciones.insert(pregunta_posicion, nueva_opcion)
                    break
                else:
                    print("Has seleccionado una posicion que no se encuentra disponible. ")
                    print("Recuerda que la posición debe ser mayor que -1 y menor a la ultima posicion")

    def __str__(self):
        return f"{self.__titulo}:{self.__opciones} "

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__titulo}:{self.__opciones} )"
