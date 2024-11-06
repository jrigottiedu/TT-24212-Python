"""
Suma de números naturales

Desarrollá una función que calcule la suma de los números naturales hasta un número dado 
utilizando un bucle for. 
La suma de los números naturales hasta el número n se define como la suma de 
todos los números enteros positivos desde 1 hasta n.

Por ejemplo, la suma de los números naturales hasta 6 es 1 + 2 + 3 + 4 + 5 + 6 = 21.

La función debe recibir un número entero n y devolver la suma de los números naturales hasta n.



Tips: 

¡Usá range()!
"""

START = 0
STEP = 1
suma = 0  # acumulador
stop = int(input("Ingrese la longitud de la lista de números naturales: "))
for numero_natural in range(START, stop, STEP):  # 0..stop, saltos de 1
    suma += numero_natural

print(f"Suma de 0 a {stop}: {suma}")
