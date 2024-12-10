# ARMAMOS UN ARCHIVO DESDE CERO SEGUN LOS REQUERIMIENTOS FINALES

# IMPORTAMOS FUNCIONES
from funciones_menu import *
from funciones_database import db_crear_tabla_productos


# Declaramos la funcion principal main
def main():
    # Inicializamos la base de datos y creamos la tabla (si no existe)
    db_crear_tabla_productos()

    # Cuerpo de la función main
    while True:
        # menu_mostrar_opciones() muestra y retorna la opcion seleccionada por el usuario
        opcion = menu_mostrar_opciones()
        print("Usted selcciono: ", opcion)

        if opcion == "1":
            menu_registrar_producto()
        elif opcion == "2":
            menu_mostrar_productos()
        elif opcion == "3":
            menu_actualizar_producto()
        elif opcion == "4":
            menu_eliminar_producto()
        elif opcion == "5":
            menu_buscar_producto()
        elif opcion == "6":
            menu_reporte_bajo_stock()
        elif opcion == "7":
            print("Gracias por usar nuestra App")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

        continuar = input(
            "\nIngrese 's' para salir o cualquier tecla para conitnuar: "
        ).lower()  # pausa para que el usuario pueda ver
        if continuar == "s":
            print("\nGracias por usar nuestra App")
            break


# ******************************************************************
# INVOCAMOS A LA FUNCION PRINCIPAL
# ******************************************************************
main()  # invocar o llamar a la funcion main()
