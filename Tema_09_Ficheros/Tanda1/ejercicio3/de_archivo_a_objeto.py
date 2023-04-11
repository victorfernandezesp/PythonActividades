"""
        Ejercicio 3:

            Modifica el ejercicio de POO que gestiona una cuenta bancaria con movimientos, de forma que añadas a la
            clase un método para guardar todos los datos de la cuenta bancaria (número, saldo y movimientos) en un
            fichero elegido por el cliente, y un nuevo constructor que reciba como parámetro un fichero como el anterior
            y cree el objeto con esos datos. Pruébalo con un programa.

            P.D.- Usa excepciones para controlar el manejo de ficheros y en caso de no poder operar dar el mensaje de
            error correspondiente.

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
