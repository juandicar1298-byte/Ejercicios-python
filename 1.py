def al():
    try:

        x = int(input("Ingrese el primer número entero: "))
        y = int(input("Ingrese el segundo número entero: "))
        z = int(input("Ingrese el tercer número entero: "))


        sum = x + y + z
        average = sum / 3


        print("La suma total es:", sum)
        print("El promedio es:", int(average))
        
    except ValueError:
        print("Debes ingresar un numero valido")


if __name__ == "__main__":
    al()