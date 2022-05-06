while True:
    try:
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese otro número: "))
        division = num1 / num2
        print("La division del primer numero con el segundo es: ", division)

        while True:
            continuar = input("¿Desea continuar? (Si/No): ")
            if continuar == "Si" or continuar == "si":
                break
            elif continuar == "No" or continuar == "no":
                exit()
            else:
                print("Ingrese una opción válida")

    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except ValueError:
        print("No es un número, porfavor ingrese un número")