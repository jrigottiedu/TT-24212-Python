# Lista para almacenar los productos
productos = []


# Función principal para el sistema de inventario (NO ELIMINAR)
def main():
    # AQUÍ PUEDES COMENZAR A DESARROLLAR LA SOLUCIÓN

    # defino variable para corte de while
    opcion = 0
    while opcion != 3:
        # Muestro opciones en pantalla
        print("\nMenú de Gestión de Productos")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Salir")

        # Solicito ingreso de opcion

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            # Agrego productos al inventario

            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            producto = [nombre, cantidad]
            productos.append(producto)
            print(productos[0])

        elif opcion == 2:

            # Listo inventario

            if len(productos) == 0:
                print("El inventario está vacío.")
            else:
                print("\nInventario actual:")
                indice = 0
                while indice < len(productos):
                    print(
                        f"Nombre: {productos[indice][0]}, Cantidad: {productos[indice][1]}"
                    )
                    indice += 1

        elif opcion == 3:

            # finalizo proceso
            print("¡Hasta luego!")

        else:

            print("Opción inválida. Por favor, seleccione una opción válida.")


# Ejecución de la función main() - (NO ELIMINAR)
if __name__ == "__main__":
    main()
