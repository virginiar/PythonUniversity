# Manejo de cadenas

# Dividir una cadena split() (parsing)
cadena = 'Hola Mundo'
palabras = cadena.split()
print(palabras)

# Buscar con find
posicion = cadena.find('Mundo')  # devolver el valor de 5
print(f'Posición de la cadena Mundo: {posicion}')

# Reemplazar con replace
nueva_cadena = cadena.replace('Mundo', 'Amigo')
print(f'Nueva cadena reemplazada: {nueva_cadena}')

# Multiplicación de cadenas
cadena = 'Hola '
resultado_multiplicacion_cadenas = cadena * 3
print(f'Resultado multplicación de cadenas: {resultado_multiplicacion_cadenas}')

# Strip - limpiar una cadena

cadena = '...Hola Mundo.....'
cadena_limpia = cadena.strip('.')
print(f'Cadena limpia de caracteres al inicio y al final: {cadena_limpia}')
