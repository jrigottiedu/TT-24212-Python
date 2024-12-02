import math
import random

numero = 4.7
redondeo = math.floor(numero)
print(f"{numero} redondeado es: {redondeo}")

factorial = math.factorial(5)
print(f"El factorial de 5 es: {factorial}")

raiz = math.sqrt(16)
print(f"La raiz de 16 es: {raiz:.1f}")


numero_aletorio = random.randint(1, 10)
for number in range(5):
    print(random.randint(1, 10))

colores = ["rojo", "verde", "azul", "amarillo"]
for number in range(5):
    print(random.choice(colores))
