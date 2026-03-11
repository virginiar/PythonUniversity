# Ticket de Venta de una compra en un supermercado
print('*** Generación de ticket de venta ***')
precio_leche = float(input('Precio de la leche: '))
precio_pan = float(input('Precio del pan: '))
precio_lechuga = float(input('Precio de la lechuga: '))
precio_platanos = float(input('Precio de los plátanos: '))
descuento_porcentaje = int(input('¿Aplicar algún descuento(%)? '))

# Calcular el subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Aplicar el descuento
descuento = subtotal * (descuento_porcentaje / 100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Calcular el impuesto (16%)
impuesto = subtotal_con_descuento * .16

# Cálculo total de la compra (incluyendo impuestos)
coste_total_compra = subtotal_con_descuento + impuesto

# Generar el ticket de venta
print(f'''
--- Ticket de Venta ---
Subtotal: {subtotal:.2f}€
Descuento: {descuento}€ ({descuento_porcentaje}%)
Subtotal con descuento: {subtotal_con_descuento:.2f}€
Impuesto (16%): {impuesto:.2f}€
Coste total de la compra: {coste_total_compra:.2f}€
''')
