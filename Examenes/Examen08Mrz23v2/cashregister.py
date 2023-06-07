"""
Clase CashRegister examen.
@author Victor Fernandez España
Curso 2022-2023
"""
from datetime import datetime

from typeguard import typechecked


@typechecked
class CashRegister:
    __listado_de_fechas = []
    __numero_operaciones = 0

    def __init__(self):
        self.__saldo_caja = 0

    @property
    def saldo_caja(self):
        return self.__saldo_caja

    def add(self, cantidad: float, concepto: str, fechayhora: datetime):
        pass
