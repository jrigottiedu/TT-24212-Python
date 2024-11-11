"""
Diccionarios

Parejas clave-valor


# Lista de productos
productos = ["manzana", "kiwi", "durazno"]
cantidades = [10, 30, 5]

# Definimos la estructura de la lista_productos:
# producto[0]: "nombre"
# producot[1]: "cantidad"
lista_productos = [["manzana", 10], ["kiwi", 30], ["durazno", 5]]
# print(lista_productos)
for producto in lista_productos:
    print(f"Producto: {producto[0]}, Cantidad: {producto[1]}")


"""

# declaracion e inicializacion de un diccionario
producto = {"nombre": "Manzana", "cantidad": 10}
print(producto)

"""
# Acceder a los valores del diccionario version_1 []
print("Accedemos a los valores del diccionario usando []")
print(producto["nombre"])  # clave "nombre" devuelve "manzana"
print(producto["cantidad"])  # clave "cantidad" devuelve 10


# Acceder a los valores del diccionario version_2 método get
print("Accedemos a los valores del diccionario usando get")
print(producto.get("nombre"))  # clave "nombre" devuelve "manzana"
print(producto.get("cantidad"))  # clave "nombre" devuelve 10


# Actualizar valores de nuestro diccionario
print(f"\nActualizamos cantidad actual {producto.get("cantidad")} a 25 ")
producto["cantidad"] = 25
print(f"Nuevo valor {producto.get("cantidad")} ")

print(f"\nActualizamos cantidad actual {producto.get("cantidad")} a 35 ")
producto.update({"cantidad": 35})
print(f"Nuevo valor {producto.get("cantidad")} ")


# Actualizar valores de nuestro diccionario
print(f'\nAgregamos el par clave "precio" con el valor 1500')
producto["precio"] = 1500
print(producto)


# Eliminar un valor de nuestro diccionario
print(f"\nEliminamos la clave cantidad precio usando del")
del producto["precio"]
print(producto)

producto["precio"] = 1500
print(f"\nEliminamos la clave cantidad precio usando pop")
producto.pop("precio")
print(producto)

"""

# Recorremos o iteramos un diccionario
print("\nfor clave in producto:")
for clave in producto:
    # print(f"clave: {clave} - {producto[clave]}")
    print(f"{clave} - {producto.get(clave)}")

print("\nfor clave in producto.keys():")
for clave in producto.keys():
    # print(f"clave: {clave} - {producto[clave]}")
    print(clave)

print("\nfor clave in producto.values():")
for valor in producto.values():
    # print(f"clave: {clave} - {producto[clave]}")
    print(valor)

print("\nfor clave, valor in producto.items():")
for clave, valor in producto.items():
    # print(f"clave: {clave} - {producto[clave]}")
    print(f"{clave}: {valor}")


"""
lista_productos = []

# Diccionario producto_1
producto_1 = {
    "nombre": "Manzana",
    "cantidad": 10,
}

lista_productos.append(producto_1)

# Diccionario producto_2
producto_2 = {
    "nombre": "Kiwi",
    "cantidad": 35,
}

lista_productos.append(producto_2)

print(f"{lista_productos[0][]}")
"""
