print("\n\n")

print("<" * 30 + ">" * 30)
print("<" * 30 + ">" * 30 + "\n\n")
print("\t" + "SISTEMA DE CONTROL DE INVENTARIO\n\n")
print("<" * 30 + ">" * 30)
print("<" * 30 + ">" * 30)
print("\n")
import sqlite3 as sql

# /// CREAMOS LA BASE DEDATOS UTILIZADA POR EL SISTEMA ///


def crear_base_de_datos():

    conx = sql.connect("inventario.db")
    cursor = conx.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS productos (
               ID_PRODUCTO integer primary key autoincrement, 
               NOMBRE_PRODUCTO text,
               DESCRIPCION text,
               CANTIDAD integer,
               PRECIO real,
               CATEGORIA text)
               """
    )

    conx.commit()
    conx.close()


# ///  DEFINIMOS EL MENU DE OPCIONES DEL SISTEMA ///
# ///  CAPTURAMOS LA FUNCION A EJECUTAR SEGUN LA OPCION ELEGIDA //==

# opcion = 0


def menu_sistema():

    # opc = [ 1, 2, 3, 4, 5, 6, 7 ]

    opc = range(8)

    print(f" 1 - Alta de productos en el inventario\n")
    print(f" 2 - Actualizacion de un producto del inventario\n ")
    print(f" 3 - Baja de productos del inventario\n")
    print(f" 4 - Consulta de stock de un producto especifico \n")
    print(f" 5 - Busqueda de producto por ID - Nombre - Categoria\n")
    print(f" 6 - Informe  de stock del inventario\n")
    print(f" 7 - Salida\n")

    opcion = input(f" Seleccione una opción numerica: ")

    if opcion.isdigit():
        opcion = int(opcion)

    while (opcion not in opc) or (opcion == 0):

        print("\n")
        opcion = input(" Opcion ingresada invalida, ingrese una nueva opcion:")

        if opcion.isdigit():
            opcion = int(opcion)

    # print(opcion)

    # tipop = type( opcion)

    # print(tipop)
    return opcion


# /// FUNCION ALTA DE UN PRODUCTO EN EL INVENTARIO ///
# /// CAPTURO LOS DATOS DEL PRODUCTOS EN UN DICCIONARIO Y LOS INSERTO EN LA BASE DE DATOS ///
# /// SE EJECUTA MIENTRAS QUIERA INGRESAR PRODUCTOS ///


def alta_de_producto():
    while True:
        nombre = str(input(f" Ingrese el nombre del producto: "))
        descripcion = input(f"Ingrese su descripción: ")
        cantidad = int(input(f"Ingrese la cantidad : "))
        precio = float(input(f"Ingrese el precio del producto: "))
        categoria = input(f"Ingrese la categoría del producto: ")

        producto = {
            "nombre": nombre,
            "descripcion": descripcion,
            "cantidad": cantidad,
            "precio": precio,
            "categoria": categoria,
        }

        print("\n")
        print(f"Ud. ha ingresado el sigueinte articulo \n")
        """
        print("-" * 90)
        print(f"NOMBRE\t\t", "DESCRIPCION\t\t", "CANTIDAD\t", "PRECIO\t\t", "CATEGORIA")
        print("-" * 90)
        print("\n")
        """

        for datos in producto.values():

            print(f"{datos}")

        print("\n")

        confirma = input(f"Confirma el alta s/n ? :").lower()
        produ = []
        produ = list(producto.values())

        if confirma == "s":
            conx = sql.connect("inventario.db")
            cursor = conx.cursor()
            cursor.execute(
                """INSERT INTO PRODUCTOS (NOMBRE_PRODUCTO, DESCRIPCION, CANTIDAD, PRECIO, CATEGORIA) VALUES (?,?,?,?,?)""",
                produ,
            )
            conx.commit()
            conx.close()
        else:
            print("No se ha realizado el alta del producto")

        continua = input(f"\n\n Ingrese s/S o n/N si desea o no agregar otro producto :").lower()
        if continua == "n":
            return


def actualizacion_de_producto():

    amodificar = []

    nombre_buscado = input(f"\n Ingrese el nombre del producto a modificar: ")
    consulta = " ( SELECT ID_PRODUCTO, NOMBRE_PRODUCTO , CANTIDAD FROM PRODUCTOS  WHERE NOMBRE_PRODUCTO = ?)"
    conex = sql.connect("inventario.db")
    cursor = conex.cursor()
    cursor.execute(consulta, nombre_buscado)
    amodificar = cursor.fetchall()
    print(amodificar)
    id_prod_mod = int(input(f"\n Ingrese el ID del producto a modificar: "))
    campo = str(input(f"\n Ingrese el campo que desea modificar: "))

    if campo.lower() == "cantidad":
        cant_nueva = int(input(f"\n Ingrese la nueva cantidad: "))
        cursor.execute(
            """UPDATE productos SET CANTIDAD = WHERE ID_PRODUCTO = id_prod_mod""", amodificar
        )


# print(f" {indice}\t\t{datos['nombre']}\t\t{datos['descripcion']}\t{datos['cantidad']}\t\t{datos['precio']}\t\t{datos['categoria']}\n\n")
# print("Producto registrado con el código", indice,"\n")


crear_base_de_datos()


# print(opmenu)

while True:
    opmenu = menu_sistema()
    if opmenu == 1:
        print(f" Ha elegido la Opción 1 - Alta de productos en el inventario\n")
        alta_de_producto()

    elif opmenu == 2:
        print(f" Ha elegido la Opción 2 - Actualizacion de un producto del inventario\n")
        actualizacion_de_producto()
    elif opmenu == 3:
        break
    else:
        print(" Opción no válida, por favor vuelva a intentarlo \n")
