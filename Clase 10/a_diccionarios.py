import os


def clear_terminal():
    # Para Windows
    if os.name == "nt":
        os.system("cls")
    # Para Linux y macOS
    else:
        os.system("clear")


# Diccionarios

# Parejas clave-valor

clear_terminal()  # Limpia la terminal
"""
# estructura 0: nombre, 1: cantidad, 2: precio
productos = ["manzana", 10, 1500]
print(f"lista productos {productos}")
"""

# producto = {"nombre": "manzana", "cantidad": 10}
"""
print(f"diccionario productos {producto}")

# acceder a los valores de un diccionario []
print("Accedemos a los valores con []")
print(producto["nombre"])  # [clave]
print(producto["cantidad"])  # [clave]

# acceder a los valores de un diccionario get
print("Accedemos a los valores con get")
print(producto.get("nombre"))
print(producto.get("cantidad"))


clear_terminal()
# Actualizar
print(producto.get("cantidad"))  # 10
producto["cantidad"] = 20  # actualizo a 20
print(producto.get("cantidad"))

# update
producto.update({"cantidad": 30})  # actualizo a 30
print(producto.get("cantidad"))


# agregar
print("original", producto)
producto["precio"] = 1500
print("agregado de precio", producto)


# Lista => []
lista = ["manzana", 10, 1500]  # referencia es el indice
lista[1] = 20
# 0: manzana
# 1: kiwi
# Diccionario => {}
diccionario = {
    "nombre": "manzana",
    "cantidad": 10,
    "precio": 1500,
}  # referencia es la clave
diccionario["cantidad"] = 20

# frutax es la clave : valor
# fruta1 es manzana
# fruta2 es kiwi

plantilla_producto ={
    "nombre": None,
    "cantidad": None,
    "precio": None,
}

"""

diccionario_producto = {
    "nombre": "manzana",
    "cantidad": 10,
}
# print(diccionario_producto["nombre"])
# print(diccionario_producto["cantidad"])
for claves in diccionario_producto.keys():  #
    print(claves)
    # print(f"{clave}: {diccionario_producto[clave]}")
    # print(f"{clave} - {values}")

for values in diccionario_producto.values():  #
    print(values)
    # print(f"{clave}: {diccionario_producto[clave]}")
    # print(f"{clave} - {values}")

for items in diccionario_producto.items():  #
    print(f"{items[0]} {items[1]}")
    # print(f"{clave}: {diccionario_producto[clave]}")
    # print(f"{clave} - {values}")
