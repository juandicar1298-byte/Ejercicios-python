precio = int(input("ingrese el precio del producto: "))

porcentaje_descuento = int(input("ingrese el porcentaje del descuento: "))

descuento = precio * (porcentaje_descuento / 100)

precio_final = precio - descuento 

print("el precio final con descuento es : ", precio_final)