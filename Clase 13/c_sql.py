import sqlite3

conexion = sqlite3.connect("inventario.db")
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()
cursor.execute("SELECT * FROM productos")
resultados = cursor.fetchall()

if not resultados:
    print("No hay registros que mostrar")
else:
    print(resultados)
    for registro_obj in resultados:
        registro = dict(registro_obj)
        for key, value in registro.items():
            print(f"{key} :  {value}")

conexion.commit()
conexion.close()
