print('*** Manejo de funciones ***')


# 1. Definir una función llamada saludar
def saludar(mensaje):
    print(f'Mensaje recibido: {mensaje}')
    return 'Terminó ok la ejecución de la función saludar'


# 2. Llamar la función (ya tiene que estar definida)
argumento = 'Hola desde la función saludar'
valor_devuelto = saludar(argumento)
print(f'Valor devuelto de la función: {valor_devuelto}')
