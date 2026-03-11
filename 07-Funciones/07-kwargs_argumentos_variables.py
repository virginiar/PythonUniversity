# args - arguments - tupla
# kwargs - keyword arguments (key, value), dict
print('*** Argumentos variables por llave ***')


def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args}. Más info: {kwargs}')


# Llamamos a la función
superheroe_superpoderes('Spiderman', 'Instinto Arácnido', edad=17, empresa='Marvel')
superheroe_superpoderes('Spiderman', 'Armadura', 'Playboy', edad=45)
superheroe_superpoderes('Mi vecino', personalidad='¡Buena onda!')
