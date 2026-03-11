print('*** Sistema de autenticación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario_ingresado = input('¿Cuál es tu usuario? ')
password_ingresado = input('¿Cuál es tu password? ')

datos_correctos = (USUARIO_VALIDO == usuario_ingresado
                   and PASSWORD_VALIDO == password_ingresado)

print(f'¿Datos correctos? {datos_correctos}')
