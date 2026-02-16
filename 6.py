producto = input("ingrese el nombre del producto: ")
precio_unitario = int(input("ingrese el precio unitario: "))
cantidad = int(input("ingrese la cantidad comprada: "))

total = precio_unitario * cantidad

print("producto:", producto)
print("total a pagar:", total)