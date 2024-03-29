"""
    Ejercicio 9:
       Nos hemos enterado de que la clase datetime. Date ha sido comprometida y tenemos que crear una clase nueva para
       almacenar fechas locales (Date), en este caso la clase será mutable (los objetos pueden cambiar el día, mes o
       año). Los objetos de la clase Fecha son fechas de tiempo y se crean de la forma:

        f1 = Date(1, 10, 2020)  # almacena el 1 de octubre de 2020
        f2 = Date(f1)  # almacena una copia de la fecha almacenada en f1

        Para simplificar consideraremos que las fechas son todas a partir del 1 de enero del año 1.

        Si al constructor se le pasan valores incorrectos lanzaremos la excepción ValueError.

        Crea métodos para:

        - Sumar y restar días a la fecha.

        - Restar fechas. Devuelve el número de días comprendidos entre ambas.

        - Comparar la fecha almacenada con otra.

        - Saber si el año de la fecha almacenada es bisiesto.

        - Obtener el día de la semana de una fecha concreta.

        - El método __str__() devuelve una cadena con el formato "<día del mes> de <nombre del mes> de <año>".


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""


class Fecha:
    def __init__(self, dia, mes=None, ano=None):
        if isinstance(dia, Fecha):
            if mes is not None or ano is not None:
                raise TypeError("Un objeto creado por otro objeto, no puedes pasarle mas de un parametro")
            other = dia
            self.__dia = int(other.dia)
            self.__mes = int(other.mes)
            self.__ano = int(other.ano)

        else:
            self.__dia = int(dia)
            self.__mes = int(mes)
            self.__ano = int(ano)

        self.__comprueba_fecha(self.__dia, self.mes, self.__ano)

    @property
    def dia(self):
        return self.__dia

    @property
    def mes(self):
        return self.__mes

    @property
    def ano(self):
        return self.__ano

    @dia.setter
    def dia(self, value: int):
        self.__comprueba_fecha(value, self.mes, self.__ano)
        self.__dia = value

    @mes.setter
    def mes(self, value: int):
        self.__comprueba_fecha(self.__dia, value, self.__ano)
        self.__mes = value

    @ano.setter
    def ano(self, value: int):
        self.__comprueba_fecha(self.__dia, self.mes, value)
        self.__ano = value

    def __comprueba_fecha(self, dia, mes, ano):
        if ano < 1:
            raise ValueError("La fecha no puede ser menor que el 1 de enero del año 1.")
        if 1 > mes > 12:
            raise ValueError("El mes introducido no es correcto.")
        if self.es_bisiesto():
            match mes:
                case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                    if not 1 <= dia <= 31:
                        raise ValueError("La fecha introducida no es correcta.")

                case 4 | 6 | 9 | 11:
                    if not 1 <= dia <= 30:
                        raise ValueError("La fecha introducida no es correcta.")

                case 2:
                    if not 1 <= dia <= 29:
                        raise ValueError("La fecha introducida no es correcta.")

        else:
            match mes:
                case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                    if not 1 <= dia <= 31:
                        raise ValueError("La fecha introducida no es correcta.")

                case 4 | 6 | 9 | 11:
                    if not 1 <= dia <= 30:
                        raise ValueError("La fecha introducida no es correcta.")

                case 2:
                    if not 1 <= dia <= 28:
                        raise ValueError("La fecha introducida no es correcta.")

    def __suma_1_dia(self):
        if self.es_bisiesto():
            match self.__mes:
                case 1 | 3 | 5 | 7 | 8 | 10:
                    if 30 >= self.__dia:
                        self.__dia += 1
                    else:
                        self.__dia = 1
                        self.__mes += 1

                case 4 | 6 | 9 | 11:
                    if 29 >= self.__dia:
                        self.__dia += 1
                    else:
                        self.__dia = 1
                        self.__mes += 1

                case 2:
                    if 29 > self.__dia:
                        self.__dia += 1
                    else:
                        self.__dia = 1
                        self.__mes += 1

                case 12:
                    if 30 >= self.__dia:
                        self.__dia += 1
                    else:
                        self.__dia = 1
                        self.__mes = 1
                        self.__ano += 1

        else:
            match self.__mes:
                case 1 | 3 | 5 | 7 | 8 | 10:
                    if 30 >= self.__dia:
                        self.__dia += 1
                    else:
                        self.__dia = 1
                        self.__mes += 1

                case 4 | 6 | 9 | 11:
                    if 29 >= self.__dia:
                        self.__dia += 1
                    else:
                        self.__dia = 1
                        self.__mes += 1
                case 2:
                    if 28 > self.__dia:
                        self.__dia += 1
                    else:
                        self.__dia = 1
                        self.__mes += 1

                case 12:
                    if 30 >= self.__dia:
                        self.__dia += 1
                    else:
                        self.__dia = 1
                        self.__mes = 1
                        self.__ano += 1

    def __resta_1_dia(self):
        if self.es_bisiesto():
            match self.__mes:
                case 5 | 7 | 8 | 10 | 12:
                    if 2 <= self.__dia:
                        self.__dia -= 1
                    else:
                        self.__dia = 31
                        self.__mes -= 1

                case 4 | 6 | 9 | 11:
                    if 2 <= self.__dia:
                        self.__dia -= 1
                    else:
                        self.__dia = 30
                        self.__mes -= 1

                case 2:
                    if 29 > self.__dia >= 2:
                        self.__dia -= 1
                    else:
                        self.__dia = 30
                        self.__mes -= 1
                case 3:
                    if 2 <= self.__dia:
                        self.__dia -= 1
                    else:
                        self.__dia = 29
                        self.__mes -= 1

                case 1:
                    if 2 <= self.__dia:
                        self.__dia -= 1
                    else:
                        self.__dia = 31
                        self.__mes = 12
                        self.__ano -= 1

        else:
            match self.__mes:
                case 5 | 7 | 8 | 10 | 12:
                    if 2 <= self.__dia:
                        self.__dia -= 1
                    else:
                        self.__dia = 31
                        self.__mes -= 1

                case 4 | 6 | 9 | 11:
                    if 2 <= self.__dia:
                        self.__dia -= 1
                    else:
                        self.__dia = 30
                        self.__mes -= 1

                case 2:
                    if 29 > self.__dia >= 2:
                        self.__dia -= 1
                    else:
                        self.__dia = 30
                        self.__mes -= 1
                case 3:
                    if 2 <= self.__dia:
                        self.__dia -= 1
                    else:
                        self.__dia = 28
                        self.__mes -= 1

                case 1:
                    if 2 <= self.__dia:
                        self.__dia -= 1
                    else:
                        self.__dia = 31
                        self.__mes = 12
                        self.__ano -= 1

    def sumar_dias(self, num_dias):
        for i in range(num_dias):
            self.__suma_1_dia()

    def restar_dias(self, num_dias):
        for i in range(num_dias):
            self.__resta_1_dia()

    def __sub__(self, other):
        if isinstance(other, Fecha):
            num_dias_comprendidos = 0
            if self > other:
                while self != other:
                    self.__suma_1_dia()
                    num_dias_comprendidos += 1
                    if self == other:
                        return num_dias_comprendidos
            elif self < other:
                while self != other:
                    other.__suma_1_dia()
                    num_dias_comprendidos += 1
                    if self == other:
                        return num_dias_comprendidos
            else:
                return num_dias_comprendidos

    def __junta_fechas(self):
        return self.__ano * 10000 + self.__mes * 100 + self.__dia

    def __eq__(self, other: 'Fecha'):
        aux_fecha1 = self.__junta_fechas()
        aux_fecha2 = other.__junta_fechas()
        return aux_fecha1 == aux_fecha2

    def __ne__(self, other: 'Fecha'):
        return not self == other

    def __lt__(self, other: 'Fecha'):
        aux_fecha1 = self.__junta_fechas()
        aux_fecha2 = other.__junta_fechas()
        return aux_fecha1 > aux_fecha2

    def __gt__(self, other: 'Fecha'):
        return (not self == other) and (not self < other)

    def __le__(self, other: 'Fecha'):
        return not self > other

    def __ge__(self, other: 'Fecha'):
        return not self < other

    def es_bisiesto(self):
        return self.__ano % 4 == 0 and self.__ano % 100 != 0 or self.__ano % 400 == 0

    def obtener_dia_semana(self):
        fecha_base = Fecha(1, 1, 1)  # Fue lunes (o eso dicen)
        dia = (self - fecha_base) % 7
        num_dia = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        print(num_dia[dia])

    def __mes_con_letra(self):
        nom_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
                     "Noviembre", "Diciembre"]
        return nom_meses[self.__mes - 1]

    def __str__(self):
        return f"{self.__dia} de {self.__mes_con_letra()} de {self.__ano} "

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dia}, {self.__mes}, {self.__ano})"
