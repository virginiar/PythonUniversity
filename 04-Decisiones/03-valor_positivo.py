print('*** Revisión de valor positivo ***')
numero = int(input('Proporciona un número: '))

if numero > 0:
    print(f'Es positivo: {numero}')
elif numero < 0:
    print(f'Es negativo: {numero}')
else:
    print(f'Es cero: {numero}')
