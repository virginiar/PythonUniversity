import os.path
import re

from contacto import Contacto


class GestionContactos:
    NOMBRE_ARCHIVO = 'agenda.txt'

    def __init__(self):
        self.contactos = []
        # Revisar si ya existe el archivo agenda
        # Si ya existe, obtenemos los contactos del archivo
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.contactos = self.obtener_contactos()
        # Sino, cargamos algunos snacks iniciales
        else:
            self.cargar_contactos_iniciales()

    def obtener_contactos(self):
        contactos = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for linea in archivo:
                    nombre, telefono, email = linea.strip().split(',')
                    contacto = Contacto(nombre, telefono, email)
                    contactos.append(contacto)
        except Exception as e:
            print(f'Error al leer archivo de contactos: {e}')
        return contactos

    def cargar_contactos_iniciales(self):
        contactos_iniciales = [
            Contacto('Juan', '900101010', 'juan@mail.com'),
            Contacto('María', '900202020', 'mariag@mail.com'),
            Contacto('Pedro', '900303030', 'pedro@mail.com')
        ]
        self.contactos.extend(contactos_iniciales)
        self.guardar_contactos_archivo(contactos_iniciales)

    def guardar_contactos_archivo(self, contactos):
        try:
            with open(self.NOMBRE_ARCHIVO, 'w') as archivo:
                for contacto in contactos:
                    archivo.write(f'{contacto.escribir_contacto()}\n')
        except Exception as e:
            print(f'Error al guardar contactos en archivo: {e}')

    @staticmethod
    def validar_correo(correo):
        """Valida el formato del correo electrónico con una expresión regular."""
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, correo)

    def agregar_contacto(self, contacto):
        if not contacto.nombre or not contacto.telefono or not contacto.correo:
            print("[Error]: Todos los campos son obligatorios.")
            return
        if not self.validar_correo(contacto.correo):
            print("[Error]: Formato de correo electrónico inválido.")
            return
        self.contactos.append(contacto)
        self.guardar_contactos_archivo(self.contactos)

    def mostrar_contactos(self):
        if self.contactos:
            for contacto in self.contactos:
                print(contacto)
        else:
            print('No hay ningún contacto.')

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        return None

    def eliminar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            self.contactos.remove(contacto)
            self.guardar_contactos_archivo(self.contactos)
            return contacto
        return None
