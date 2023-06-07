"""
Clase CashRegister examen.
@author Victor Fernandez España
Curso 2022-2023
"""
from Examenes.Examen08Mrz23.movement import Movement
from datetime import datetime


class CashRegister:
    __listado_movimientos = []
    __ultima_fecha = datetime.now()
    __ultima_cantidad = []

    def __init__(self):
        self.__saldo_caja = 0

    def add(self, movimiento: 'Movement'):
        if 0 > (self.__saldo_caja + movimiento.amount):
            raise ValueError("La caja no puede tener saldo negativo")
        if movimiento.date_time > CashRegister.__ultima_fecha:
            raise ValueError("La fecha no puede ser anterior a la guardada")
        self.__saldo_caja += movimiento.amount
        CashRegister.__listado_movimientos.append(movimiento)
        CashRegister.__ultima_fecha = movimiento.date_time
        CashRegister.__ultima_cantidad = movimiento.amount

    def delete_last(self):
        CashRegister.__listado_movimientos.pop(len(CashRegister.__listado_movimientos))
        self.__saldo_caja -= CashRegister.__ultima_cantidad[len(CashRegister.__ultima_cantidad)]
        CashRegister.__ultima_cantidad.pop(CashRegister.__ultima_cantidad[len(CashRegister.__ultima_cantidad)])

    def balance(self):
        return f"{self.__saldo_caja}"

    def __str__(self):
        return f"{CashRegister.__listado_movimientos}{self.__saldo_caja}"

    def __repr__(self):
        return f"{CashRegister.__listado_movimientos}{self.__saldo_caja}"
