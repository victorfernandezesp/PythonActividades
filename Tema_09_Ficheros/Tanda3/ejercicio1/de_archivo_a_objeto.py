"""
        Ejercicio 2:

            Modifica el ejercicio de la cuenta corriente para que el método que almacena en un fichero el estado del
            objeto guarde el objeto entero y el que lo recupera lo restaure. En esta versión no le pasamos nombre de
            fichero al método a la hora de guardarlo, usará el número de cuenta corriente para ello.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import pickle


class Archivo_A_Objeto:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.guardar = self.convertir_archivo_a_objeto()

    def convertir_archivo_a_objeto(self):
        with open(self.nombre_archivo, 'rb') as f:
            return pickle.load(f)
