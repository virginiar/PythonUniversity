print('*** Sistema de calificaciones ***')

calificacion = float(input('Proporciona una calificación entre 0 y 10: '))
calificacion_letra = ''
# Revisamos si está en los siguientes rangos
if 9 <= calificacion <= 10:
    calificacion_letra = 'A'
elif 8 <= calificacion < 9:
    calificacion_letra = 'B'
elif 7 <= calificacion < 8:
    calificacion_letra = 'C'
elif 6 <= calificacion < 7:
    calificacion_letra = 'D'
elif 0 <= calificacion < 6:
    calificacion_letra = 'F'
else:
    calificacion_letra = 'Calificación incorrecta'
# Imprimimos el resultado
print(f'Calificación {calificacion} es equivalente a {calificacion_letra}')