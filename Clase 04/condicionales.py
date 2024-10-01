"""
Estructuras de control - Condicionales
IF, ELSE; ELIF
"""

numero_1 = 20
numero_2 = 30


# print(f"comparamos numero_1 y numero_2 {numero_1 == numero_2}")

# comparando por igual
if numero_1 == numero_2:
    print(f"Los numeros son iguales {numero_1} {numero_2}")

# comparo por distinto
if numero_1 != numero_2:
    print(f"Los numeros son diferentes {numero_1} {numero_2}")


# comparamos usando if-else
if numero_1 == numero_2:  # if + condicion + :

    print(f"Los numeros son iguales {numero_1} {numero_2}")  # si la condicion se cumple
else:
    print(
        f"Los numeros son diferentes {numero_1} {numero_2}"
    )  # cuando la condicion NO se cumple
