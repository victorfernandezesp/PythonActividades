"""
    Ejercicio 12:
        Implementa la clase Mobile como subclase de Terminal (la clase del ejercicio anterior que ya no hace
        falta modificar). Cada móvil lleva asociada una tarifa que puede ser “rata”, “mono” o “bisonte” (debes controlar
        esto). El coste por minuto es de 6, 12 y 30 céntimos respectivamente. Se tarifican los segundos exactos.
        La tarifa se puede cambiar. Obviamente, cuando un móvil llama a otro, se le cobra al que llama, no al que recibe
        la llamada. A continuación se proporciona el contenido del programa principal que usa esta clase y el resultado
        que debe aparecer por pantalla. El total tarificado debe aparecer con dos decimales.

        Programa principal:

        m1 = Mobile("678112233", "rata")
        m2 = Mobile("644744469", "mono")
        m3 = Mobile("622328909", "bisonte")
        print(m1)
        print(m2)
        m1.call(m2, 320)
        m1.call(m3, 200)
        m2.call(m3, 550)
        print(m1)
        print(m2)
        print(m3)
        Salida:

        N.º 678 11 22 33 - 0 s de conversación - tarificados 0,00 euros
        N.º 644 74 44 69 - 0 s de conversación - tarificados 0,00 euros
        N.º 678 11 22 33 - 520 s de conversación - tarificados 0,52 euros
        N.º 644 74 44 69 - 870 s de conversación - tarificados 1,10 euros
        N.º 622 32 89 09 - 750 s de conversación - tarificados 0,00 euros

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from typeguard import typechecked


@typechecked
class Tarifas:
    __tarifas_disponibles = ["rata", "mono", "bisonte"]
    __costo_tarifas = [6, 12, 30]

    def __init__(self, nombre: str):
        self.nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str):
        self.comprueba_tarifa(value)
        self.__nombre = value

    @staticmethod
    def comprueba_tarifa(value):
        if value not in Tarifas.__tarifas_disponibles:
            raise ValueError("Tarifa desconocida")

    @staticmethod
    def anade_tarifa(nombre_tarifa: str, costo_tarifa: int):
        Tarifas.__tarifas_disponibles.append(nombre_tarifa)
        Tarifas.__costo_tarifas.append(costo_tarifa)

    @staticmethod
    def tarifica(tarifa, minutos):
        if tarifa == "rata":
            return (minutos * Tarifas.__costo_tarifas[0]) / 100

        elif tarifa == "mono":
            return (minutos * Tarifas.__costo_tarifas[1]) / 100

        else:
            return (minutos * Tarifas.__costo_tarifas[2]) / 100

    def __repr__(self):
        return f"{self.__nombre}"
