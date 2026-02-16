talleres = int(input("Ingrese la nota de talleres: "))
parcial = int(input("Ingrese la nota del examen parcial: "))
final = int(input("Ingrese la nota del examen final: "))

nota_definitiva = (talleres * 0.30) + (parcial * 0.30) + (final * 0.40)

print("La nota definitiva es:", nota_definitiva)