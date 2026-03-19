from Reto2.contacto import Contacto
from Reto2.gestion_contactos import GestionContactos


class AppGestionContactos:
    def __init__(self):
        self.gestion_contactos = GestionContactos()

    def mostrar_menu(self):
        print('*** Sistema de gestión de contactos ***')
        while True:
            try:
                print(f'''Menú:
                1. Agregar contacto
                2. Mostrar contactos
                3. Buscar contacto
                4. Eliminar contacto
                5. Salir
                ''')
                option = int(input('Seleccione una opción (1-5): '))
                if option == 1:
                    self.agregar_contacto()
                elif option == 2:
                    self.mostrar_contactos()
                elif option == 3:
                    self.buscar_contacto()
                elif option == 4:
                    self.eliminar_contacto()
                elif option == 5:
                    print('¡Hasta pronto!')
                    break
                else:
                    print('Opción no válida. Seleccione una opción del 1 al 5.')
            except Exception as e:
                print(f'Ocurrió un error: {e}')

    def agregar_contacto(self):
        nombre = input('Nombre: ')
        telefono = input('Teléfono: ')
        correo = input('Correo: ')
        contacto = Contacto(nombre, telefono, correo)
        self.gestion_contactos.agregar_contacto(contacto)

    def mostrar_contactos(self):
        print('Listado de contactos:')
        self.gestion_contactos.mostrar_contactos()

    def buscar_contacto(self):
        nombre = input('Nombre a buscar: ')
        contacto = self.gestion_contactos.buscar_contacto(nombre)
        if contacto:
            print(contacto)
        else:
            print(f'Contacto {nombre} no encontrado.')

    def eliminar_contacto(self):
        nombre = input('Nombre a eliminar: ')
        contacto = self.gestion_contactos.eliminar_contacto(nombre)
        if contacto:
            print(f'Contacto {nombre} eliminado.')
        else:
            print(f'Contacto {nombre} no encontrado')


if __name__ == '__main__':
    agenda = AppGestionContactos()
    agenda.mostrar_menu()
