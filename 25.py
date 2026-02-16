numero_ventas = int(input("Ingrese el número de ventas realizadas: "))

total_vendido = 0

for i in range(numero_ventas):
    valor = float(input("Ingrese el valor de la venta: "))
    total_vendido += valor

promedio = total_vendido / numero_ventas

print("El total vendido es:", total_vendido)
print("El promedio por venta es:", promedio)