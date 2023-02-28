"""
    Ejercicio 10:
        Crea la clase abstracta Vehicle, así como las clases Bike y Car como subclases de la primera. Para la clase
        Vehicle, crea los atributos de clase vehicles_created y total_kilometers, así como el atributo de instancia
        kilometers_traveled.

        En la clase Vehicle crea un método para viajar (travel) que incremente los kilómetros recorridos. En la clase
        Bike haz un método para hacer el caballito y en la clase Car otro para quemar rueda.

        Prueba las clases creadas mediante un programa con un menú (usando la clase de la tanda anterior) como el que se
        muestra a continuación:

        VEHÍCULOS
        =========
        1. Anda con la bicicleta
        2. Haz el caballito con la bicicleta
        3. Anda con el coche
        4. Quema rueda con el coche
        5. Ver kilometraje de la bicicleta
        6. Ver kilometraje del coche
        7. Ver kilometraje total
        8. Salir


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

from Tema_06_POO.Tanda3POO.ejercicio10.car import Car
from Tema_06_POO.Tanda3POO.ejercicio10.bike import Bike
from Tema_06_POO.Tanda3POO.ejercicio10.vehiculo import Vehicle

import sys

from bibliotecafunciones.util.menu import Menu

SALIDA_DEL_PROGRAMA_CON_EXITO = 0

menu1 = Menu("VEHÍCULOS",
             "Anda con la bicicleta.",
             "Haz el caballito con la bicicleta.",
             "Anda con el coche.",
             "Quema rueda con el coche.",
             "Ver kilometraje de la bicicleta.",
             "Ver kilometraje del coche.",
             "Ver kilometraje total.")

bici = Bike()
coche = Car()

while True:
    option = menu1.escoger()
    match option:

        case 1:
            bici.viajar(int(input("¿Cuantos Km anda la bicicleta?")))

        case 2:
            bici.hacer_caballito()

        case 3:
            coche.viajar(int(input("¿Cuantos Km anda el Coche?")))

        case 4:
            coche.quema_rueda()

        case 5:
            print(bici.kilometros_viajados)

        case 6:
            print(coche.kilometros_viajados)

        case 7:
            print(Vehicle.kilometros_totales)

        case 8:
            sys.exit(SALIDA_DEL_PROGRAMA_CON_EXITO)
