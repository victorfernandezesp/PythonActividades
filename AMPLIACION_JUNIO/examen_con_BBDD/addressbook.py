"""
    Examen 22-Mayo-2023
    Clase AddressBook

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import xml.etree.ElementTree as ET
from time import sleep

from Victor_Fernandez_Espana.contact import Contact


class LongitudNombreArchivoXMLError(ValueError):
    def __init__(self, archivo):
        super().__init__(f"La longitud del nombre del archivo no puede ser menor de 5(ej: x.xml). Recibido ({archivo}).")
        self.archivo = archivo

class AddressBook:
    def __init__(self, databasename, username, password):
        self.__base_de_datos = databasename
        self.__usuario =  username
        self.__contrasena = password

        self.__lista_agenda = []
        self.__lista_de_nombres = []
        if databasename != "":
            self.__cargar_datos_de_bbdd_internamente(self.__base_de_datos)

    @property
    def lista_agenda(self):
        return self.__lista_agenda.copy()

    def pasa_xml_a_agenda(self, database, nombre_de_fichero):
        archivo = ET.parse(nombre_de_fichero)
        root = archivo.getroot()
        for i in range(len(root)):
            nombre_contacto = root[i].get("nombre")
            telefono_contacto = root[i][0].text
            correo_contacto = root[i][1].text
            direccion_contacto = root[i][2].text
            self.alta_contacto(database, nombre_contacto, telefono_contacto, correo_contacto, direccion_contacto)

    def alta_contacto(self, database, nombre, telefono, correo, direccion = ""):
        import mysql.connector
        try:
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user=f"{self.__usuario}",
                password=f"{self.__contrasena}",
                database=f'{database}'

            )
            mi_cursor = mydb.cursor()
            sql = "INSERT INTO agenda (nombre_nuevo_contacto, telefono_nuevo_contacto, correo_nuevo_contacto, direccion_nuevo_contacto) VALUES (%s, %s, %s, %s)"
            val = (nombre,telefono, correo, direccion)
            mi_cursor.execute(sql, val)
            mydb.commit()
            self.__lista_agenda.append(Contact(nombre, telefono, correo, direccion))
            self.__lista_de_nombres.append(nombre)

        except PermissionError:
            print(f"Problemas con la Base de Datos, revisa los permisos de tu usuario de la Base de Datos.")
            sleep(5)

    def baja_contacto(self, database, nombre):
        for i in self.__lista_agenda:
            if i.nombre == nombre:
                self.__lista_agenda.remove(i)
                self.__lista_de_nombres.remove(i.nombre)

        import mysql.connector
        try:
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user=f"{self.__usuario}",
                password=f"{self.__contrasena}",
                database=f'{database}'

            )
            mi_cursor = mydb.cursor()
            sql = "DELETE FROM agenda WHERE nombre_nuevo_contacto = %s"
            val = (nombre, )
            mi_cursor.execute(sql, val)
            mydb.commit()
        except PermissionError:
            print(f"Problemas con la Base de Datos, revisa los permisos de tu usuario de la Base de Datos.")
            sleep(5)

    def listar_contactos(self):
        lista_interna = []
        for i in self.__lista_agenda:
            lista_interna.append(i)
        return lista_interna

    def __cargar_datos_de_bbdd_internamente(self, database):
        import mysql.connector
        try:
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user=f"{self.__usuario}",
                password=f"{self.__contrasena}",
                database=f'{database}'

            )
            mi_cursor = mydb.cursor()
            mi_cursor.execute("SELECT * FROM agenda")

            mi_resultado = mi_cursor.fetchall()
            for i in mi_resultado:
                if i[0] not in self.__lista_de_nombres:
                    nombre = i[0]
                    telefono = i[1]
                    correo = i[2]
                    direccion = i[3]

                    self.__lista_agenda.append(Contact(nombre, telefono, correo, direccion))
                    self.__lista_de_nombres.append(nombre)


        except PermissionError:
            print(f"Problemas con la Base de Datos, revisa los permisos de tu usuario de la Base de Datos.")
            sleep(5)

    def exportar_a_xml(self, fichero_donde_se_anaden_contactos):
        tree = ET.parse(fichero_donde_se_anaden_contactos)
        root = tree.getroot()
        for i in self.__lista_agenda:
            nombre_contacto = i.nombre
            telefono_contacto = i.telefono
            correo_contacto = i.correo
            direccion_contacto = i.direccion

            contacto = ET.Element('contacto', {'nombre': nombre_contacto})
            telefono = ET.SubElement(contacto, 'telefono')
            telefono.text = telefono_contacto

            correo = ET.SubElement(contacto, 'correo')
            correo.text = correo_contacto

            direccion = ET.SubElement(contacto, 'direccion')
            direccion.text = direccion_contacto

            root.append(contacto)
            ET.indent(root, space='    ')
            tree.write(fichero_donde_se_anaden_contactos, encoding='unicode')



