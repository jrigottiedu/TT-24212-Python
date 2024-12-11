import sqlite3

# DECLARACION DE CONSTANTES
# ruta_db = r"C:\Users\JPy\Documents\TT24212 Python\TT-24212-Python\Clase 15\inventario.db"
ruta_db = r"D:\Dailutb\TT 2C2024 Python\Clases\Clase 15\inventario.db"

"""
db_crear_tabla_productos()

Esta función utiliza sqlite3 para crear/conectarse con la base "inventario.db" y crea la tabla productos
"""


def db_crear_tabla_productos():
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()  # siempre igual
    cursor.execute(
        """ 
CREATE TABLE IF NOT EXISTS productos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT NOT NULL,
descripcion TEXT,
categoria TEXT NOT NULL,
cantidad INTEGER NOT NULL,
precio REAL NOT NULL
)
"""
    )
    conexion.commit()
    conexion.close()


"""
db_insertar_producto(producto)

1. recibe como argumento un diccionario con las clave/valor de cada campo de la tabla
2. inserta los datos en la tabla productos
"""


def db_insertar_producto(nombre, descripcion, categoria, cantidad, precio):
    try:
        conexion = sqlite3.connect(ruta_db)
        cursor = conexion.cursor()  # siempre igual
        # query = "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?, ?, ?, ?, ?)"
        query = "INSERT INTO productos  VALUES (NULL, ?, ?, ?, ?, ?)"
        placeholder = (nombre, descripcion, categoria, cantidad, precio)
        cursor.execute(query, placeholder)
        conexion.commit()
    except Exception as error:
        print(f"Error: {error}")
    finally:
        conexion.close()


"""
db_get_productos()

1. lee todos los datos de la tabla productos
2. retorna una lista de tuplas con los datos de la tabla
"""


def db_get_productos():
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "SELECT * FROM productos"
    cursor.execute(query)
    lista_productos = cursor.fetchall()
    conexion.close()
    return lista_productos


"""
db_get_producto_by_id(id)

1. busca en la tabla el registro segun el id
2. retorna una tupla con el resultado
"""


def db_get_producto_by_id(id):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "SELECT * FROM productos WHERE id = ?"
    placeholders = (id,)
    cursor.execute(query, placeholders)
    producto = cursor.fetchone()
    conexion.close()
    return producto


"""
db_actualizar_producto(id, nueva_cantidad)

1. actualiza la cantidad del producto según el id
"""


def db_actualizar_producto(id, nueva_cantidad):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "UPDATE productos SET cantidad = ? WHERE id = ?"
    placeholders = (nueva_cantidad, id)
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()


"""
db_eliminar_producto(id)

1. elimina de la tabla el producto con el id que recibe como argumento
"""


def db_eliminar_producto(id):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "DELETE FROM productos WHERE id = ?"
    placeholders = (id,)
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()


"""
db_get_productos_by_condicion(minimo_stock)

1. retornar una lista_producto con aquellos registros cuya cantidad < minimo_stock
"""


def db_get_productos_by_condicion(minimo_stock):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "SELECT * FROM productos WHERE cantidad < ?"
    placeholders = (minimo_stock,)
    cursor.execute(query, placeholders)
    lista_productos = cursor.fetchall()
    conexion.close()
    return lista_productos
