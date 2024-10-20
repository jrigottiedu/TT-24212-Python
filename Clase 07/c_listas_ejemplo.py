# Declaramos una lista
lista_jugadores = []
lista_jugadores.clear()

# Comenzamos con un Bucle del tipo while, que se ejecutará hasta que el usuario ingrese 3
while True:
    print("\n ---------- *** ----------")
    print("Plantel Selección Argentina 2024")
    print("Menú de opciones\n")

    print("1. Alta de Jugador")
    print("2. Mostrar plantel")
    print("3. Salir")

    # Pedimos al usuario que ingrese una opción
    opcion = input("\nIngrese su opción: ")

    # Opción 1: Alta de Jugador
    # debemos solicitar nombre del jugador y camiseta
    if opcion == "1":
        jugador_nombre = input("Nombre y Apellido del jugador: ")
        jugador_camiseta = int(input("Camiseta: "))
        elemento_jugador = [jugador_nombre, jugador_camiseta]
        lista_jugadores.append(elemento_jugador)
    # Opción 2: Mostrar Juagdores
    elif opcion == "2":
        # Bloque de codigo para mostrar el plantel
        # print(f"Jugador: {jugador_nombre} - Camiseta: {jugador_camiseta}")
        indice = 0
        while indice < len(lista_jugadores):
            print(f"Jugador: {lista_jugadores[indice][0]} - Camiseta: {lista_jugadores[indice][1]}")
            indice += 1
    # Opción 3: el Bucle while debe terminar para salir
    elif opcion == "3":
        break

    # Si la opción ingresada no es válida, mostramos un mensaje de error
    else:
        print("Opcione  no válida, por favor intente de nuevo")
