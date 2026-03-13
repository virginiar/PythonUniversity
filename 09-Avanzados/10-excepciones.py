print('*** Manejo de excepciones ***')


def dividir(numerador, denominador):
    try:
        # Revisamos si el denominador es igual a 0
        if denominador == 0:
            raise Exception('El denominador es igual a 0')
        resultado = numerador / denominador
        print(f'Resultado de la división: {resultado}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    else:
        print(f'No ocurrió ningún error')
    finally:
        print(f'Terminamos de procesar la excepción\n')
    # except ZeroDivisionError:
    #     print('Error: No se puede dividir entre cero')
    # except TypeError:
    #     print('Error: Los operandos deben ser numéricos')


# Ejemplo de uso
dividir(10, 2)
dividir(10, 0)
dividir(10, '0')
