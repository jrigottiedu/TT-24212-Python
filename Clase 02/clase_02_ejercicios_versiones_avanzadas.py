"""
Alternativa ejercicio 1
"""

# productos = {
#     "Lechuga": 1000,
#     "tomate": 1200,
#     "cebolla": 900,
# }

# print("El precio de los productos es:")
# for key, value in productos.items():
#     precio_producto = "El precio de " + key + "es de: " + str(value)
#     print(precio_producto)


"""
Alternativa ejercicio 2
"""

# meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
# ingresos = 0
# for mes in meses:
#     ingreso = input(f"Ingrese el ingreso del mes de  {mes} ")
#     ingresos += int(ingreso)
# promedio = ingresos / len(meses)
# print(f"El promedio de los ingresos es de: {promedio:.2f}")


"""
Alternativa ejercicio 1
"""
lista_compras = []


def agregar_producto():
    producto = input("Ingresá el producto que querés agregar: ")
    lista_compras.append(producto)
    print(f"El producto '{producto}' ha sido agregado a la lista.")


def ver_lista():
    if len(lista_compras) == 0:
        print("La lista del supermercado está vacía.")
    else:
        print("Lista de compras en el supermercado:")
        for producto in lista_compras:
            print("- " + producto)


while True:
    print("\nOpciones:")
    print("1. Agregar un producto")
    print("2. Ver lista de productos")
    print("3. Salir")

    opcion = input("Ingresá una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        ver_lista()
    elif opcion == "3":
        print("¡Chau!")
        break
    else:
        print("Opción inválida. Por favor, ingresá 1, 2 o 3.")
