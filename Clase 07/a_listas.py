"""
Colecciones / Arreglos

LISTAS


# Declaracion tipo de datos simples
numero = None
cadena = ""

# Declaracion de una lista vacia
lista = []

# Declara e inicializar una lista
lista = ["manzana", "pera", "kiwi"]
print(lista)

print(lista[1])  # imprime el primer elemento de la lista

print()

indice = 0
while indice < len(lista):  # len(lista) nos devuelve la longitud => 3
    # print(lista[indice])
    print(f"lista[{indice}]: {lista[indice]}")
    indice += 1

    """

# estructua 0: producto, 1: cantidad, 2: bool
elemento_0 = ["manzana", 10, False]
elemento_1 = ["pera", 5, False]

# Armar una lista de lista
# Lista de productos a comprar
lista_super = [elemento_0, elemento_1]
# print(lista_super)

"""
iteramos la lista_super de forma básica
indice = 0  # declaro el contador / indice
while indice < len(lista_super): #len(lista_super) => 2
    print(lista_super[indice])
    indice += 1


# iteramos la lista_super de forma completa
indice = 0  # declaro el contador / indice
while indice < len(lista_super):  # len(lista_super) => 2
    elemento = lista_super[indice]
    print(f"Producto: {elemento[0]}, cantidad: {elemento[1]}")
    indice += 1


indice_lista = 0  # declaro el contador / indice
while indice_lista < len(lista_super):  # len(lista_super) => 2
    # guardo cada elemento de lista_super en elemento
    elemento = lista_super[indice_lista]
    # permite recorrer la sub-lista
    indice_sublista = 0
    # itero la sublista
    while indice_sublista < len(elemento):
        # imprimo cada elemento de la sub-lista
        print(f"{elemento[indice_sublista]}")
        # incremento el contador de la sub-lista
        indice_sublista += 1
    # incremento el contador de la lista
    indice_lista += 1
"""

# Introduccion a metodos
lista = ["manxana", "pera", "kiwi"]
lista[0] = "manzana"
lista[3] = "banana"
print(lista)
