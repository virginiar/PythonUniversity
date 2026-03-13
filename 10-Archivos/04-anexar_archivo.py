print('*** Anexar información a un archivo ***')

nombre_archivo = 'mi_archivo.txt'

with open(nombre_archivo, 'a') as archivo:
    # Anexar información al archivo
    archivo.write('Anexando información ... \n')
    archivo.write('Saliendo de anexar información...\n')

print(f'Se ha anexado información al archivo {nombre_archivo}')
