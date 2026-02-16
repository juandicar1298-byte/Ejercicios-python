cantidad_productos = int(input("ingrese la cantidad del producto: "))

total = 0

for i in range(cantidad_productos):
    precio = int(input("ingrese el precio del producto: "))
    total = total + precio 

print("el total de la compra es: ", total )
    