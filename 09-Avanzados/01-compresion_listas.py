print('*** Comprensión de listas ***')

# Filtrar solo los números pares y generar una nueva lista con estos valores

numeros = range(1, 10 + 1)
# Sin usar comprensión de listas
numeros_pares = []
# Iteramos cada elemento de la lista
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(f'Números pares del 1 al 10: {numeros_pares}')

# Usando comprensión de listas
# sintaxis: nueva_lista = [expresion for elemento in iterable if condicion]
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print(f'Números pares del 1 al 10: {numeros_pares}')
