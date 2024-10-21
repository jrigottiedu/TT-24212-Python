"""
Colecciones / Arreglos

LISTAS
"""

# Declaramos una lista vacía
lista = []

# Declaramos e inicializamos una lista
lista = ["manzana", "durazno", "melon"]
print(f"\nlista es: {lista}")

# Cada elemento de la lista tiene una posición
# Accedemos a cada elemento a través de un índice
print(f"\nlista[0] es: {lista[0]}")
print(f"lista[1] es: {lista[1]}")
print(f"lista[2] es: {lista[2]}")

# Recorremos la lista con un while
print()
indice = 0
while indice < len(lista):
    print(f"lista[{indice}] es: {lista[indice]}")
    indice += 1


# Los elementos pueden ser Heterogéos
# [0]: producto [1]: cantidad [2]: precio [3]: estado
lista = ["durazno", 2, 350.99, False]


# lista de listas => tabla o matriz
elemento_0 = ["manzana", 2, 350.99, False]
elemento_1 = ["durazno", 3, 450.99, False]

lista_super = [elemento_0, elemento_1]
print(lista_super)

indice = 0
while indice < len(lista_super):
    # print(f"Elemento {indice+1}: {lista_super[indice]}")
    print(f"Producto: {lista_super[indice][0]} Cantidad: {lista_super[indice][1]}")
    indice += 1


# Métodos
elemento_0[5] = 5
elemento_0[3] = True
# elemento1[4] = "comprar en Carrefour" #IndexError: list assignment index out of range
