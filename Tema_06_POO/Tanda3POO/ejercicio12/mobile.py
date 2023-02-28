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

        Nº 678 11 22 33 - 0s de conversación - tarificados 0,00 euros
        Nº 644 74 44 69 - 0s de conversación - tarificados 0,00 euros
        Nº 678 11 22 33 - 520s de conversación - tarificados 0,52 euros
        Nº 644 74 44 69 - 870s de conversación - tarificados 1,10 euros
        Nº 622 32 89 09 - 750s de conversación - tarificados 0,00 euros

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from typeguard import typechecked

from Tema_06_POO.Tanda3POO.ejercicio11.terminal import Terminal


@typechecked
class Mobile(Terminal):

    def __init__(self, num: str, tarifa: str):
        super().__init__(num)
        if tarifa not in ["rata", "mono", "bisonte"]:
            raise ValueError("Tarifa desconocida")
        self.__tarifa = tarifa
        self.__tarificado = 0
        self.__segundos = 0

    @property
    def tarificado(self):
        return self.__tarificado

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, value: str):
        if value not in ["rata", "mono", "bisonte"]:
            raise ValueError("Tarifa desconocida")
        self.__tarifa = value

    @property
    def segundos(self):
        return self.__segundos

    def llama(self, other, segundos):
        self.__segundos += segundos
        other.__segundos += segundos
        a_tarifar = segundos / 60

        if self.__tarifa == "rata":
            self.__tarificado += (a_tarifar * 6) / 100

        elif self.__tarifa == "mono":
            self.__tarificado += (a_tarifar * 12) / 100

        else:
            self.__tarificado += (a_tarifar * 30) / 100

    def __repr__(self):
        return f"{self.__class__.__name__} Nº {self.numero} - {self.__segundos}s de conversación - tarificados " \
               f"{self.__tarificado} euros"
