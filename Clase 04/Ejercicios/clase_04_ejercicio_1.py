"""
Ticket de la compra

Escribir un programa que solicite el nombre, la cantidad y el valor unitario de tres productos.
Luego, debe calcular el importe de IVA (21%) de cada producto.
Por último, debe mostrar en la terminal el ticket de la operación con todos los datos de la compra. 
"""

"""
Ticket de la compra


Escribir un programa que solicite el nombre, la cantidad y el valor unitario de tres productos.
Luego, debe calcular el importe de IVA (21%) de cada producto.
Por último, debe mostrar en la terminal el ticket de la operación con todos los datos de la compra.
"""


# Declaración / Inicialización de variables
PORCENTAJE_IVA = 0.21  # variable en uppercase para indicar que es una constante


# Entrada
print("Ingrese los datos del primer producto: ")
nombre_producto_1 = input("Nombre: ")
valor_producto_1 = float(input("Valor: "))
cantidad_producto_1 = int(input("Cantidad: "))
print("Ingrese los datos del segundo producto: ")
nombre_producto_2 = input("Nombre: ")
valor_producto_2 = float(input("Valor: "))
cantidad_producto_2 = int(input("Cantidad: "))
print("Ingrese los datos del tercer producto: ")
nombre_producto_3 = input("Nombre: ")
valor_producto_3 = float(input("Valor: "))
cantidad_producto_3 = int(input("Cantidad: "))


# Proceso
subtotal_producto_1 = valor_producto_1 * cantidad_producto_1
subtotal_producto_2 = valor_producto_2 * cantidad_producto_2
subtotal_producto_3 = valor_producto_3 * cantidad_producto_3
subtotal = subtotal_producto_1 + subtotal_producto_2 + subtotal_producto_3
impuesto_iva = subtotal * PORCENTAJE_IVA
total = subtotal + impuesto_iva


# Salida
print("Ticker de compra")
print(
    f"Nombre de producto {nombre_producto_1}\t (cantidad {cantidad_producto_1}) \t importe {subtotal_producto_1} pesos"
)
print(
    f"Nombre de producto {nombre_producto_2}\t (cantidad {cantidad_producto_2}) \t importe {subtotal_producto_2} pesos"
)
print(
    f"Nombre de producto {nombre_producto_3}\t (cantidad {cantidad_producto_3}) \t importe {subtotal_producto_3} pesos"
)
print()
print(f"Subtotal de productos: {subtotal}")
print(f"Inpuesto IVA 21%: {impuesto_iva:.2f}")
print(f"TOTAL: {total:.2f}")
