# ARMAMOS UN ARCHIVO DESDE CERO SEGUN LOS REQUERIMIENTOS FINALES


# ******************************************************************
# DECLARACION DE VARIABLES
# ******************************************************************
# a fines practicos (temporalmente hasta que implementemos Base de Datos) almacenamos en lista o diccionario
lista_productos = []  # esta variable lista luego se reemplazar por una tabla en SQLite
inventario = {}  # esta variable diccionario luego se reemplazar por una tabla en SQLite
# Modelo del diccionario para un producto dado
producto = {
    "nombre": None,
    "descripcion": None,
    "cantidad": 100,
    "precio": None,
    "categoria": None,
}


# ******************************************************************
# DECLARACION DE FUNCIONES
# ******************************************************************


# Funcion que muestra el menú
def mostrar_menu():
    print("-" * 30)
    print(" Menú principal")
    print("-" * 30)
    print(
        """
        1. Agregar producto
          2. Mostrar producto
          3. Actualizar
          4. Eliminar
          5. Buscar producto
          6. Reporte bajo Stock
          7. Salir
        """
    )
    opcion = input("Ingrese la opción deseada: ")
    # Agregan un modulo de validacion para evitar errores - PENDIENTE
    # retorno un Str
    return opcion


# Función alta o registro de producto
def registrar_producto():
    # Cuerpo de la función
    print("REGISTRO DE PRODUCTO")
    # pedir al usuario (variable_nombre, descripcion....)
    # agregar validacion...
    # usar un metodo de sqlite, que le vamos a pasar esta query
    """
    INSERT INTO productos (
        nombre, 
        descripcion, 
        categoria, 
        cantidad, 
        precio) 
    VALUES 
    (variable_nombre, 'Un clásico atemporal de Antoine de Saint-Exupéry', 'infantil', 50, 1580 )
    """


# Función que muestra los productos almacenados en nuestro inventario
def mostrar_productos():
    # Cuerpo de la función
    print("VISUALIZAR PRODUCTOS")


# Función que actualiza los datos de un producto especifico
def actualizar_producto():
    # Cuerpo de la función
    print("ACTUALIZAR UN PRODUCTO")


# Función que elimina un producto especifico
def eliminar_producto():
    # Cuerpo de la función
    print("ELIMINAR UN PRODUCTO")


# Función que busca un producto especifico
def buscar_producto():
    # Cuerpo de la función
    print("BUSCAR UN PRODUCTO")


# Función que genera un reporte de Bajo Stock
def reporte_bajo_stock():
    # Cuerpo de la función
    # Pedir al usuario que ingrese el umbral_minimo_stock
    print("REPORTE DE BAJO STOCK")


def main():  # funcion o cuerpo principal del archivo Python
    while True:
        opcion = mostrar_menu()  # esta aca dentro opcion = input("Elija una opción: ")
        print("Usted selcciono: ", opcion)  # imprime la opción seleccionada por el usuario

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "7":
            print("Adios")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

        continuar = input(
            "Presione 's' para continuar..."
        ).lower()  # pausa para que el usuario pueda ver
        if continuar == "s":
            break


# ******************************************************************
# INVOCAMOS A LA FUNCION PRINCIPAL
# ******************************************************************
main()  # invocar o llamar a la funcion main()
