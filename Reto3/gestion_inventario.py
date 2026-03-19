from conexion import Conexion
from producto import Producto


class GestionInventario:
    SELECCIONAR = 'SELECT * FROM producto ORDER BY id;'
    BUSCAR = 'SELECT * FROM producto WHERE nombre=%s;'
    INSERTAR = 'INSERT INTO producto(nombre, cantidad, precio, categoria) VALUES(%s, %s, %s, %s);'
    ACTUALIZAR = 'UPDATE producto SET nombre=%s, cantidad=%s, precio=%s, categoria=%s WHERE id=%s;'
    ELIMINAR = 'DELETE FROM producto WHERE id=%s;'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla producto
            productos = []
            for registro in registros:
                producto = Producto(registro[0], registro[1],
                                    registro[2], registro[3], registro[4])
                productos.append(producto)
            return productos
        except Exception as e:
            print(f'Ocurrió un error al seleccionar productos: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def buscar(cls, nombre):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (nombre,)
            cursor.execute(cls.BUSCAR, valores)
            registro = cursor.fetchall()[0]
            producto = Producto(registro[0], registro[1],
                                registro[2], registro[3], registro[4])
            return producto
        except Exception as e:
            print(f'Ocurrió un error al buscar un producto: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al insertar un producto: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre, producto.cantidad,
                       producto.precio, producto.categoria, producto.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al actualizar un producto: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al eliminar un producto: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    # Insertar cliente
    # producto1 = Producto(nombre='Mesas', cantidad=3, precio=149.99, categoria='Salón')
    # productos_insertados = GestionInventario.insertar(producto1)
    # print(f'Productos insertados: {productos_insertados}')
    # producto2 = Producto(nombre='Silla', cantidad=12, precio=39.99, categoria='Salón')
    # productos_insertados = GestionInventario.insertar(producto2)
    # print(f'Productos insertados: {productos_insertados}')

    # Actualizar producto
    # producto_actualizar = Producto(2, 'Mesa 150x100 nogal', 3, 149.99, 'Salón')
    # productos_actualizados = GestionInventario.actualizar(producto_actualizar)
    # print(f'Productos actualizados: {productos_actualizados}')

    # Eliminar producto
    # producto_eliminar = Producto(id=2)
    # productos_eliminados = GestionInventario.eliminar(producto_eliminar)
    # print(f'Productos eliminados: {productos_eliminados}')

    # Buscar producto
    # producto2 = Producto(nombre='Silla', cantidad=12, precio=39.99, categoria='Salón')
    # productos_insertados = GestionInventario.insertar(producto2)
    # print(f'Productos insertados: {productos_insertados}')
    # producto_buscar = "Silla"
    # productos_encontrados = GestionInventario.buscar(producto_buscar)
    # print(f'Productos encontrados: {productos_encontrados}')

    # Seleccionar los productos
    productos = GestionInventario.seleccionar()
    for producto in productos:
        print(producto)
