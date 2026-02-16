total_compra = int(input("ingrese el valor total de la compra: "))

if total_compra > 200000:
    descuento = total_compra  * 0.10
    total_final = total_compra - descuento
else:
    # sin descuento
    total_final = total_compra

print("el valor total a pagar es: ", total_final)
