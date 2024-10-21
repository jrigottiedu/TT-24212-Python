# Declaramos variables
jugador_nombre = None
jugador_camiseta = None

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

    # Opción 2: Mostrar Juagdores
    elif opcion == "2":
        # Bloque de codigo para mostrar el plantel
        print(f"Jugador: {jugador_nombre} - Camiseta: {jugador_camiseta}")

    # Opción 3: el Bucle while debe terminar para salir
    elif opcion == "3":
        break

    # Si la opción ingresada no es válida, mostramos un mensaje de error
    else:
        print("Opcione  no válida, por favor intente de nuevo")
