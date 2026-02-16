edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("Es menor de edad.")
elif edad < 60:
    print("Es adulto.")
else:
    print("Es adulto mayor.")