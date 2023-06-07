"""
Clase Movement examen.
@author Victor Fernandez España
Curso 2022-2023
"""
from datetime import datetime


class Movement:
    last_number = 0

    def __init__(self, amount: float, concept: str, date_time=datetime.now()):
        if amount < 0:
            raise ValueError("La cantidad debe ser positiva")
        self.number = Movement.last_number + 1
        Movement.last_number += 1
        self.__amount = amount
        self.__concept = concept
        self.__date_time = date_time

    @property
    def amount(self):
        return self.__amount

    @property
    def concept(self):
        return self.__concept

    @property
    def date_time(self):
        return self.__date_time

    def __repr__(self):
        return f"Cantidad: {self.__amount} | Concepto:{self.__concept} | Fecha: {self.__date_time}"
