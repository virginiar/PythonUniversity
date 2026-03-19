class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre.strip()
        self.telefono = telefono.strip()
        self.correo = correo.strip()

    def __str__(self):
        return f'{self.nombre}: {self.telefono} - {self.correo}'

    def escribir_contacto(self):
        return f'{self.nombre},{self.telefono},{self.correo}'
