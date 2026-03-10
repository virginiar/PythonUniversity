print('*** Desempaquetado de tuplas ***')  # unpacking

producto = ('P001', 'Camisa', 20.00)

# Desempaquetamos cada valor en variables independientes
identificador, descripcion, precio = producto

print(f'Tupla completa: {producto}')
# Valores independientes ya desempaquetados
print(f'Producto: id = {identificador}, descripción = {descripcion}, precio = {precio}')