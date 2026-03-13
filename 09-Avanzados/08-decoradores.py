print('*** Decoradores en Python ***')


def decorador(funcion):
    def wrapper(*args, **kwargs):
        print('Antes de llamar la función saludar')
        resultado = funcion(*args, **kwargs)  # llamamos a nuestra función
        print('Después de llamar la función saludar')
        return resultado

    return wrapper


@decorador
def saludar(nombre):
    print(f'Hola {nombre}')


saludar('Carlos')
