print('*** Operadores de Asignación Compuestos ***')
a, b = 10, 15
print(f'Valor inicial a: {a}, Valor inicial b: {b}')

# Operador compuesto de suma +=
a += b  # a = a + b
print(f'Operador a += b es: {a}')

# Operador compuesto de resta -=
a = 10  # Reiniciamos el valor de a
a -= b  # a = a - b
print(f'Operador a -= b es: {a}')

# Operador compuesto de multiplicación *=
a = 10  # Reiniciamos el valor de a
a *= b
print(f'Operador a *= b es: {a}')

# Operador compuesto de division /=
a = 10  # Reiniciamos el valor de a
a /= b
print(f'Operador a /= b es: {a}')
