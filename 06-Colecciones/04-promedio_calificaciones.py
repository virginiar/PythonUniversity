print('*** Promedio de calificaciones ***')

total_calificaciones = int(input('Proporciona el número de calificaciones a evaluar: '))
calificaciones = []

# Iteramos las calificaciones
for indice in range(total_calificaciones):
    calificacion = int(input(f'Calificación[{indice}] = '))
    calificaciones.append(calificacion) # Agregamos la calificación a la lista

# Imprimimos las calificaciones proporcionadas
print(f'\nLas calificaciones proporcionadas son: {calificaciones}')
# Calculamos el promedio de las calificaciones
suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones / total_calificaciones
print(f'\n Promedio de las calificaciones: {promedio}')