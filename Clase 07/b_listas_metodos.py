# Metodos de listas
lista = ["manxana", 10, "pera", "kiwi"]

# agregar otro elemento a la lista
lista.append("durazno")
lista.append(10)
print(lista)

print()
indice = 0
while indice < len(lista):
    print(f"lista[{indice}]: {lista[indice]}")
    indice += 1
print()

# remover elemento con remove
lista.remove(10)
print("\nLista despues de remover el 10", lista)

indice = 0
while indice < len(lista):
    print(f"lista[{indice}]: {lista[indice]}")
    indice += 1

# remover o quitar elementos con pop
lista.pop()  # remover el último elemento
print(lista)

lista.pop(2)  # remover el último elemento
print(lista)
