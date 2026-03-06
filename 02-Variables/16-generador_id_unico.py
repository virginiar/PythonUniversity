# Generador ID Único
# import random
from random import randint

print('*** Sistema Generador de ID Único ***')
nombre = input('¿Cuál es tu nombre? ')
nombre_2 = nombre[0:2].upper()
apellido = input('¿Cuál es tu apellido? ')
apellido_2 = apellido[0:2].upper()
anio_nacimiento = input('¿Cuál es tu año de nacimiento (YYYY)? ')  # Y - year
anio_nacimiento_2 = anio_nacimiento[2:4]
# Generar un valor aleatorio de 4 dígitos
aleatorio = randint(1000, 9999)
# Generamos el ID único
id_unico = f'{nombre_2}{apellido_2}{anio_nacimiento_2}{aleatorio}'
print(f'''\nHola {nombre}, 
    Tu nuevo número de identificación (ID) generado por el sistema es:
    {id_unico}
    ¡Felicidades!''')