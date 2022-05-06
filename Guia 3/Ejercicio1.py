while True:
    try:
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese otro número: "))
        suma = num1 + num2
        print("La suma es: ", suma)

        while True:
            continuar = input("¿Desea continuar? (Si/No): ")
            if continuar == "Si" or continuar == "si":
                break
            elif continuar == "No" or continuar == "no":
                exit()
            else:
                print("Ingrese una opción válida")

    except ValueError:
        print("No es un número, porfavor ingrese un número")
