"""
    Ejercicio 1:
        Modifica tu clase para gestionar menús de opciones en consola de forma que cuando el usuario introduzca una
        opción no entera se capture la excepción, se le advierta de que solo se admiten valores numéricos y se pida de
        nuevo la opción.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from typeguard import typechecked


@typechecked
class Menu:
    def __init__(self, titulo: str, *opciones: str):
        self.__titulo = titulo
        self.__opciones = list(opciones)
        self.__opciones.append("Terminar")

    def __mostrar_opciones(self):
        print(f"{self.__titulo}:")
        contador = 1
        for opcion in self.__opciones:
            print(f"{contador}. {opcion}")
            contador += 1
        print('-------------------------------------------------------------------------------------------------------')

    def escoger(self):
        self.__mostrar_opciones()
        while True:
            try:
                x = int(input("¿Que vas a seleccionar?    "))
            except ValueError:
                print("Solo se admiten valores numéricos")
                continue

            if 1 <= x <= len(self.__opciones):
                return x
            else:
                print("Ha introducido una opcion incorrecta, vuelva  a intentarlo.")

    def anadir_opciones(self, nueva_opcion, posicion):
        if posicion == len(self.__opciones):
            self.__opciones.insert(len(self.__opciones) - 1, nueva_opcion)
        else:
            while True:
                if len(self.__opciones) > posicion > -1:
                    self.__opciones.insert(posicion+1, nueva_opcion)
                    break
                else:
                    print("Has seleccionado una posicion que no se encuentra disponible. ")
                    print("Recuerda que la posición debe ser mayor que -1 y menor a la ultima posicion")

    def __str__(self):
        return f"{self.__titulo}:{self.__opciones} "

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__titulo}:{self.__opciones} )"