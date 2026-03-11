print('*** Regresar una tupla de valores desde una función ***')


# Definición de la función
def persona_mayusculas(nombre, apellido, edad):
    print('Esta función regresa varios valores (tupla)')
    return nombre.upper(), apellido.upper(), edad


# Programa principal
nombre_may, apellido_may, edad_may = persona_mayusculas('Sandra', 'Jimenez', 42)
print(f'Resultado de persona: nombre = {nombre_may}, apellido = {apellido_may}, edad = {edad_may}')
