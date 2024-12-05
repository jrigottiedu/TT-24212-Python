import sqlite3


# Función para crear la tabla productos
# IF NOT EXISTS es una excepción para que no se cree en caso que ya exista
def crear_tabla_productos():
    try:
        conexion = sqlite3.connect(
            r"C:\Users\JPy\Documents\TT24212 Python\TT-24212-Python\entregaFinal\inventario.db"
        )
        cursor = conexion.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS productos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               descripcion TEXT,
               categoria TEXT NOT NULL,
               cantidad INTEGER NOT NULL,
               precio REAL NOT NULL
            )"""
        )
        conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        conexion.close()


def insertar_registro(diccionario):
    try:
        conexion = sqlite3.connect("D:/Dailutb/TT 2C2024 Python/Clases/entregaFinal/inventario.db")
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?, ?, ?, ?, ?)",
            (
                diccionario.get("nombre"),
                diccionario.get("descripcion"),
                diccionario.get("categoria"),
                diccionario.get("cantidad"),
                diccionario.get("precio"),
            ),
        )
        conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al insertar registro: {e}")
    finally:
        conexion.close()


# Llamada a Funciones
crear_tabla_productos()

# Código para testing
# crear_tabla_productos()
# diccionario = {
#     "nombre": "manzana",
#     "descripcion": "de estación",
#     "categoria": "fruta",
#     "cantidad": 10,
#     "precio": 150,
# }
# insertar_registro(diccionario)
