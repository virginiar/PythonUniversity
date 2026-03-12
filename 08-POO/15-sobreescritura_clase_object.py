class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Sobreescribir el método __str__
    def __str__(self):
        return f'''Persona
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir. Mem. {super.__str__(self)}'''


# Código principal
persona1 = Persona('Ana', 'Martínez')
# print(persona1.__str__())  # El método str se llama automáticamente desde print
print(persona1)
