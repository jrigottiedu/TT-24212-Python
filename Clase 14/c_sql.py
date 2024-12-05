# 1. Importar el módulo sqlite3 para poder manejar la base de datos
import sqlite3

# 2. Crear y/o conectarse a la basde de datos inventario.db
conexion = sqlite3.connect(
    r"C:\Users\JPy\Documents\TT24212 Python\TT-24212-Python\entregaFinal\inventario.db"
)


# 3. Crear un cursor/puntero para interacturar con la base
cursor = conexion.cursor()

# 4. Ejecutar las consultas SQL (INSERT, SELECT, UPDATE, DELETE)
cursor.execute("SELECT * FROM productos WHERE id = 1")

# 5. Almacenar los datos de la consulta en una variable temporal resultados
# resultados = (cursor.fetchall())  # Retorna una lista de tuplas, donde cada tupla corresponde a un registro
resultados = cursor.fetchone()  # Retorna una tupla

print(resultados)
# 6. Trabajar con los resultado, mostrandolos en pantalla (PRESENTACION)
# if not resultados:
#     print("No hay registros que mostrar")
# else:
#     print(resultados)
#     for registro in resultados:
#         for campo in registro:
#             print(f"{campo}")


# 7. Hacer commit - principalmente si usaron INSERT, UPDATE O DELETE
conexion.commit()

# 8. Cerrar la conexión para cualquier consulta
conexion.close()


# Esto nos permite transformar la tupla en un diccionario
# conexion.row_factory = sqlite3.Row
# for registro_obj in resultados:
#     registro = dict(registro_obj)
#     for key, value in registro.items():
#         print(f"{key} :  {value}")
