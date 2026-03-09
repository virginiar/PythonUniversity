print('*** Aplicación de cajero automático ***')

saldo = 1000 # saldo inicial
salir = False
while not salir:
    print(f'''Operaciones que puedes realizar:
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    opcion = int(input('Escoge una opción: '))
    if opcion == 1:
        print(f'Tu saldo actual es: ${saldo:.2f}\n')
    elif opcion == 2:
        retiro = float(input('Ingresa el monto a retirar: '))
        # Validación
        if retiro <= saldo:
            saldo -= retiro  # saldo = saldo - retiro
            print(f'Tu nuevo saldo es: ${saldo:.2f}\n')
        else:
            print(f'No cuentas con el saldo suficiente. Saldo actual ${saldo:.2f}\n')
    elif opcion == 3:
        deposito = float(input('Ingresa el monto a depositar: '))
        saldo += deposito  # saldo = saldo + deposito
        print(f'Tu nuevo saldo es: ${saldo:.2f}\n')
    elif opcion == 4:
        print('Saliendo del cajero automático. ¡Hasta pronto!')
        salir = True
    else:
        print('Opción inválida. Selecciona otra opción\n')