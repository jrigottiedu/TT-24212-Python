# Metodos de listas

lista = ["manzana", "durazno", "melon"]
print(f"\nLista original {lista} \n")
# lista.append("kiwi") #Inserta un elemento al final de la lista
# lista.remove("melon") #remueve el elemento indicado
# lista.pop()  # remueve el último elemento de la lista
# lista.pop(0)  # remueve el elemtno indicado con el ídice como argumento
# lista.insert(2, "frutilla") #inserta en la posición indicada por el índice
# lista.sort()  # ordena la lista, los elementos deben ser comparables
# posicion = lista.index("durazno")
# print(posicion)

print(f"Lista modificada {lista} \n")

indice = 0
while indice < len(lista):
    print(f"lista[{indice}]: {lista[indice]}")
    indice += 1
