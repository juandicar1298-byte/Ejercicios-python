precio = int(input("ingrese el precio del producto: "))
porcentaje_descuento = int(input("ingrese el porcentaje de descuento: "))

descuento = precio * (porcentaje_descuento / 100)
precio_final = precio - descuento 
print("el valor del descuento es: ", descuento )
print("el prrecio final es: ", precio_final )