"""
    Examen 22-mayo-2023
    Clase Contact

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from typeguard import typechecked


class LongitudNombreError(ValueError):
    def __init__(self, nombre):
        super().__init__(f"El nombre no puede estar vacío.")
        self.nombre = nombre


class LongitudNumeroTelefonoError(ValueError):
    def __init__(self, telefono):
        super().__init__(f"La longitud del telefono no puede ser distinto de 9. Recibido ({len(telefono)}).")
        self.telefono = telefono


class FormatoNumeroTelefonoError(ValueError):
    def __init__(self, telefono):
        super().__init__(f"El formato de telefono recibido es incorrecto, debe empezar por 6, 7 o 9. Recibido({telefono[0]}).")
        self.telefono = telefono


class FormatoCorreoError(ValueError):
    def __init__(self, correo):
        super().__init__( f"El formato de corro recibido es incorrecto, debe contener un '@' en medio y al menos un '.'"
                          f"detras de la @. Recibido({correo}).")
        self.correo = correo


@typechecked
class Contact:

    def __init__(self, nombre, telefono, correo, direccion = ""):
        self.__comprueba_longitud_nombre(nombre)
        self.__nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    @property
    def nombre(self):
        return self.__nombre

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, value: str):
        self.__comprueba_longitud_numero(value)
        self.__comprueba_telefono_empieza_por_6_7_o_9(value)
        self.__telefono = value

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, value: str):
        self.__comprueba_correo_es_correcto(value)
        self.__correo = value

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, value: str):
        self.__direccion = value

    def __comprueba_correo_es_correcto(self, correo):
        patron = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
        resultado_de_correo = self.__extraer_numero_datos(patron, correo)
        if resultado_de_correo == 0:
            raise FormatoCorreoError(correo)

    def __comprueba_telefono_empieza_por_6_7_o_9(self, telefono):
        patron = "[679]\d{8}"
        resultado_de_telefono = self.__extraer_numero_datos(patron, telefono)
        if resultado_de_telefono == 0:
            raise FormatoNumeroTelefonoError(telefono)

    @staticmethod
    def __comprueba_longitud_numero(telefono):
        if len(telefono) != 9:
            raise LongitudNumeroTelefonoError(telefono)

    @staticmethod
    def __comprueba_longitud_nombre(nombre):
        if len(nombre) < 1:
            raise LongitudNombreError(nombre)

    @staticmethod
    def __extraer_numero_datos(patron, cadena):
        import re
        resultados = re.findall(patron, cadena)
        return len(resultados)


    def __str__(self):
        return f"Nombre: {self.__nombre} | Teléfono:{self.__telefono} | Correo: {self.__correo} | Direccion: {self.__direccion}"
