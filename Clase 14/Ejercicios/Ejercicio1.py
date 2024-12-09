import sqlite3


def main():
    # Declaración de variables
    nuevas_personas = [
        ("Esteban", 32, "Mar del Plata"),
        ("Valeria", 27, "Bahía Blanca"),
        ("Fernando", 41, "Rosario"),
        ("Carolina", 29, "La Plata"),
        ("Juan", 35, "Córdoba"),
    ]

    # Llamar/invocar a la función que crea la tabla personas
    crear_tabla_personas()

    # Iteramos la lista, y por cada tupla insertamos un registro
    for indice, persona in enumerate(nuevas_personas):
        insertar_persona(persona[0], persona[1], persona[2])
        print(f"Registro {indice} insertada con éxito")


def crear_tabla_personas():
    conexion = sqlite3.connect(
        r"C:\Users\JPy\Documents\TT24212 Python\TT-24212-Python\Clase 14\Ejercicios\base_ejercicio_14.db"
    )
    cursor = conexion.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    ciudad TEXT NOT NULL
    )
    """
    )
    conexion.commit()
    conexion.close()


def insertar_persona(nombre, edad, ciudad):
    conexion = sqlite3.connect("base_ejercicio_14.db")
    cursor = conexion.cursor()
    # cursor.execute("INSERT INTO personas (nombre, edad, ciudad) VALUES ('juan', 32, 'baires')")
    cursor.execute(
        "INSERT INTO personas (nombre, edad, ciudad) VALUES (?,?,?)", (nombre, edad, ciudad)
    )
    conexion.commit()
    conexion.close()

    # si el proceso fue ok, retorno True, sino retorno False


def reporte_bajo_stock(umbral_minimo_stock):
    conexion = sqlite3.connect("base_ejercicio_14.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE stock < ?", (umbral_minimo_stock,))
    conexion.commit()
    conexion.close()


# Cuerpo principal


def update_bajo_stock(id_producto, umbral_minimo_stock):
    conexion = sqlite3.connect("base_ejercicio_14.db")
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE FROM productos SET stock = ? WHERE id < ?", (umbral_minimo_stock, id_producto)
    )
    conexion.commit()
    conexion.close()


# Cuerpo principal

# Invocar/llamar a la función main
main()
