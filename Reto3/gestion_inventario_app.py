from gestion_inventario import GestionInventario
from producto import Producto

print('*** Sistema de Gestión de Inventario con Base de Datos ***')
opcion = None
while opcion != 5:
    print(f'''Menú:
    1. Mostrar productos
    2. Agregar producto
    3. Modificar producto
    4. Eliminar producto
    5. Buscar producto
    6. Salir''')
    opcion = int(input('Escribe tu opción (1-6): '))
    if opcion == 1:  # Listar productos
        productos = GestionInventario.seleccionar()
        print('\n*** Listado de productos ***')
        for producto in productos:
            print(producto)
    elif opcion == 2:  # Agregar producto
        nombre_var = input('Escribe el nombre: ')
        cantidad_var = int(input('Escribe la cantidad: '))
        precio_var = float(input('Escribe el precio: '))
        categoria_var = input('Escribe la categoría: ')
        productos = GestionInventario.seleccionar()
        productos_encontrados = []
        for producto in productos:
            if producto.nombre == nombre_var:
                productos_encontrados.append(producto)
                break
        if not productos_encontrados:
            producto = Producto(nombre=nombre_var, cantidad=cantidad_var,
                                precio=precio_var, categoria=categoria_var)
            productos_insertados = GestionInventario.insertar(producto)
            print(f'Se ha añadido el producto con el nombre {nombre_var}.')
        else:
            print(f'Ya existe un producto con el nombre {nombre_var}.')
    elif opcion == 3:  # Modificar producto
        id_producto_var = int(input('Escribe el id del producto a modificar: '))
        nombre_var = input('Escribe el nombre: ')
        cantidad_var = int(input('Escribe la cantidad: '))
        precio_var = float(input('Escribe el precio: '))
        categoria_var = input('Escribe la categoría: ')
        producto = Producto(id_producto_var, nombre_var, cantidad_var,
                            precio_var, categoria_var)
        productos_actualizados = GestionInventario.actualizar(producto)
        if productos_actualizados == 0:
            print(f'No se ha encontrado el producto con id {id_producto_var}.')
        else:
            print(f'Se ha modificado el producto con id {id_producto_var}.')
    elif opcion == 4:  # Eliminar producto
        id_producto_var = int(input('Escribe el id del producto a eliminar: '))
        producto = Producto(id=id_producto_var)
        productos_eliminados = GestionInventario.eliminar(producto)
        if productos_eliminados == 0:
            print(f'No se ha encontrado el producto con id {id_producto_var}.')
        else:
            print(f'Se ha eliminado el producto con id {id_producto_var}.')
    elif opcion == 5:  # Buscar un producto
        nombre_var = input('Escribe el nombre del producto a buscar: ')
        productos = GestionInventario.buscar(nombre_var)
        productos_encontrados = []
        for producto in productos:
            if producto.nombre == nombre_var:
                productos_encontrados.append(producto)
                break
        if not productos_encontrados:
            print(f'No se ha encontrado el producto con el nombre {nombre_var}.')
        else:
            print(productos_encontrados)
else:
    print('Salimos de la aplicación...')
