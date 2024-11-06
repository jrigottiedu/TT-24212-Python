codigos = ["p001", "p002", "p003"]

buscar = input("Ingrese el codigo: ")

if buscar in codigos:
    posicion = codigos.index(buscar)  # capturo el indice del codigo en mi lista
    print("Posicion encontrada: ", posicion)
else:
    print("Posicion no encontrada")  # si no lo encuentra, muestra un mensaje de
