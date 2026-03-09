print('*** Sistema de autenticación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario = input('Ingresa tu usuario: ')
password = input('Ingresa tu password: ')

if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
    print('Bienvenido al Sistema...')
elif usuario == USUARIO_VALIDO:
    print('Password erróneo, ¡favor de corregirlo!')
elif password == PASSWORD_VALIDO:
    print('Usuario erróneo, ¡favor de corregirlo!')
else:
    print('Usuario y password erróneos, ¡favor de corregirlos!')
