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
from time import sleep

from Tema_06_POO.Tanda3POO.ejercicio10.vehiculo import Vehicle


class Car(Vehicle):

    def viajar(self, kilometros):
        self.kilometros_totales += kilometros
        self.kilometros_viajados += kilometros

    @staticmethod
    def quema_rueda():
        sleep(2)
        print("IIIIIIIIIIIIIIIIIIIIIIIIII")
        sleep(1)
        print("No es Iago Aspas pero también quema rueda")
        sleep(4)

    def __repr__(self):
        return f"{self.__class__.__name__}"
