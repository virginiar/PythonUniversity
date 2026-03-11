# Factorial de un número
print('*** Factorial de un número')


# Definir la función factorial recursiva
def factorial_recursivo(numero):
    # Caso base: factorial de 0 o 1 es 1
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial {numero} es: 1')
        return 1
    # Caso recursivo, calcular factorial del número reducido en 1
    else:
        factorial_parcial = numero * factorial_recursivo(numero - 1)
        print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial


# Programa principal
if __name__ == '__main__':
    # Solicitar al usuario el número del cual desea calcular el factorial
    numero = int(input('Proporciona el número para calcular su factorial: '))
    # Verificamos si el número es negativo
    if numero < 0:
        print('El factorial no está definido para números negativos')
    else:
        # Llamamos a la función factorial_recursivo para calcular el factorial
        resultado = factorial_recursivo(numero)
        print(f'El factorial de {numero} es: {resultado}')
