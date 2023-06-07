"""
    Examen 22-Mayo-2023
    Programa de Prueba

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys
import os
import xml.etree.ElementTree as ET
from time import sleep

from AMPLIACION_JUNIO.examen_con_BBDD.addressbook import AddressBook
from AMPLIACION_JUNIO.examen_con_BBDD.menu import Menu


class NoExisteFicheroError(FileNotFoundError):
    def __init__(self, archivo):
        super().__init__(f"Lo siento pero ese nombre de archivo no existe, introduce uno que sí exista. Recibido ({archivo}).")
        self.archivo = archivo

class AccesoAlArchivoError(PermissionError):
    def __init__(self, archivo):
        super().__init__(f"Lo siento pero el acceso a ese archivo esta denegado.")
        self.archivo = archivo

class ExtensionArchivoError(ValueError):
    def __init__(self, extension):
        super().__init__(f"Lo siento pero el archivo tiene que tener la extension '.xml'.")
        self.extension = extension

def alta_contacto(nombre_de_la_bbdd, agenda):
    nombre_nuevo_contacto = input("Escribe el nombre del nuevo contacto:    ")
    telefono_nuevo_contacto = input("Escribe el telefono del nuevo contacto:    ")
    correo_nuevo_contacto = input("Escribe el correo del nuevo contacto:    ")
    direccion_nuevo_contacto = input("Escribe la direccion del nuevo contacto (Pulsa Enter para no introducirla, no es obligatoria):    ")

    agenda.alta_contacto(nombre_de_la_bbdd, nombre_nuevo_contacto, telefono_nuevo_contacto, correo_nuevo_contacto, direccion_nuevo_contacto)

def importar_archivo_desde_xml(nombre_de_la_bbdd, agenda):
    nombre_fichero_xml = input("¿Cuál es el nombre del archivo XML, desde el que quieres importar la agenda?:   ")
    comprueba_fichero(nombre_fichero_xml)
    agenda.pasa_xml_a_agenda(nombre_de_la_bbdd, nombre_fichero_xml)

def comprueba_fichero(fichero):
    try:
        fichero_comprueba = open(fichero, 'rt')
        fichero_comprueba.close()
    except FileNotFoundError:
        raise NoExisteFicheroError(fichero)
    except PermissionError:
        raise AccesoAlArchivoError(fichero)


def baja_contacto(nombre_de_la_bbdd, agenda):
    nombre_baja_contacto = input("Escribe el nombre del contacto a eliminar:    ")
    agenda.baja_contacto(nombre_de_la_bbdd, nombre_baja_contacto)



def listado_contactos(agenda):
    contactos = agenda.listar_contactos()
    for i in contactos:
        print(i)

def comprueba_si_existe_el_fichero(fichero):
    try:
        f = open(fichero, 'rt')
        f.close()
        return True
    except FileNotFoundError:
        return False

def exportar_a_xml(agenda):
    fichero = pregunta_nombre_archivo_xml_a_exportar()
    agenda.exportar_a_xml(fichero)

def pregunta_nombre_archivo_xml_a_exportar():
    while True:
        nombre_fichero = input("¿Cuál será el nombre del fichero XML?:   ")
        longitud_nombre_fichero = len(nombre_fichero) - 4
        extension = nombre_fichero[longitud_nombre_fichero:]
        if extension != ".xml":
            raise ExtensionArchivoError(extension)

        if not comprueba_si_existe_el_fichero(nombre_fichero):
            root = ET.Element('agenda')
            tree = ET.ElementTree(root)
            with open(nombre_fichero, 'wb') as f:
                tree.write(f, encoding='utf-8', xml_declaration=True)
            print(f"Fichero {nombre_fichero} creado correctamente")
            return nombre_fichero
        else:
            sobreescribe = input(f"El archivo {nombre_fichero} existe, si no desea continuar introduzca N:   ")
            if sobreescribe.upper() == "N":
                continue
            else:
                os.remove(nombre_fichero)

                root = ET.Element('agenda')
                tree = ET.ElementTree(root)
                with open(nombre_fichero, 'wb') as f:
                    tree.write(f, encoding='utf-8', xml_declaration=True)
                print(f"Fichero {nombre_fichero} creado correctamente")
                return nombre_fichero


def crear_base_datos():
    usuario_BBDD = input("¿Cuál es el nombre del usuario de la Base de Datos?:    ")
    contrasena_BBDD = input("¿Cuál es el nombre de la contraseña del usuario?:    ")

    if __comprueba_conexion(usuario_BBDD, contrasena_BBDD):
        nombre_BBDD = input("¿Cuál es el nombre de la Base de Datos?:    ")
        import mysql.connector
        try:
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user=f"{usuario_BBDD}",
                password=f"{contrasena_BBDD}"
            )
            mi_cursor = mydb.cursor()
            mi_cursor.execute(f'Create database {nombre_BBDD};')
            mi_cursor.execute(f'Use {nombre_BBDD};')
            mi_cursor.execute(f'CREATE TABLE AGENDA( nombre_nuevo_contacto VARCHAR(45) PRIMARY KEY NOT NULL, telefono_nuevo_contacto VARCHAR(45) NOT NULL, correo_nuevo_contacto VARCHAR(45) NOT NULL, direccion_nuevo_contacto VARCHAR(45));')

        except mysql.connector.DatabaseError or PermissionError:
            print(f"Problemas con la Base de Datos, revisa los permisos de tu usuario de la Base de Datos.")
            sleep(5)


def __comprueba_conexion(username, password):
    import mysql.connector
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user=f"{username}",
            password=f"{password}"
        )
        mi_cursor = mydb.cursor()
        return True
    except RuntimeError or ValueError:
        print(f"Problemas a la hora de conectar con la Base de Datos, revisa los parametros y/o el estado de la Base de Datos.")
        sleep(5)

def seleccionar_base_datos():
    usuario_BBDD = input("¿Cuál es el nombre del usuario de la Base de Datos?:    ")
    contrasena_BBDD = input("¿Cuál es el nombre de la contraseña del usuario?:    ")

    if __comprueba_conexion(usuario_BBDD, contrasena_BBDD):
        nombre_BBDD = input("¿Cuál es el nombre de la Base de Datos?:    ")
        import mysql.connector
        try:
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user=f"{usuario_BBDD}",
                password=f"{contrasena_BBDD}"
            )
            mi_cursor = mydb.cursor()
            mi_cursor.execute(f'Use {nombre_BBDD};')

        except mysql.connector.DatabaseError or PermissionError:
            print(f"Problemas con la Base de Datos, revisa los permisos de tu usuario de la Base de Datos.")
            sleep(5)
        return usuario_BBDD, contrasena_BBDD, nombre_BBDD

def main():
    SALIDA_DEL_PROGRAMA_CON_EXITO = 0
    usuario = ""
    contrasena = ""
    nombre_de_la_bbdd = ""
    selecciona_la_bbdd = False
    agenda = AddressBook(nombre_de_la_bbdd, usuario, contrasena)
    menu_anade_pregunta = Menu("AGENDA",
                 "Crear Base de Datos.",
                 "Seleccionar Base de Datos.",
                 "Alta de contacto.",
                 "Baja de contacto.",
                 "Listado de contactos.",
                 "Exportar a XML.",
                 "Importar desde XML."
                    )

    while True:
        option = menu_anade_pregunta.escoger()
        match option:

            case 1:
                crear_base_datos()
            case 2:
                usuario, contrasena, nombre_de_la_bbdd = seleccionar_base_datos()
                agenda = AddressBook(nombre_de_la_bbdd, usuario, contrasena)
                selecciona_la_bbdd = True
            case 3:
                if selecciona_la_bbdd:
                    alta_contacto(nombre_de_la_bbdd, agenda)
                else:
                    print("Primero debe seleccionar una Base de Datos, seleccione la opción 2.")
            case 4:
                if selecciona_la_bbdd:
                    baja_contacto(nombre_de_la_bbdd, agenda)
                else:
                    print("Primero debe seleccionar una Base de Datos, seleccione la opción 2.")
            case 5:
                if selecciona_la_bbdd:
                    listado_contactos(agenda)
                else:
                    print("Primero debe seleccionar una Base de Datos, seleccione la opción 2.")
            case 6:
                if selecciona_la_bbdd:
                    exportar_a_xml(agenda)
                else:
                    print("Primero debe seleccionar una Base de Datos, seleccione la opción 2.")
            case 7:
                if selecciona_la_bbdd:
                    importar_archivo_desde_xml(nombre_de_la_bbdd, agenda)
                else:
                    print("Primero debe seleccionar una Base de Datos, seleccione la opción 2.")
            case 8:
                print("¡Hasta la próxima ^_^!")
                sys.exit(SALIDA_DEL_PROGRAMA_CON_EXITO)
            case _:
                print("Ha introducido una opcion incorrecta, vuelva a intentarlo.")



if __name__ == '__main__':
    main()