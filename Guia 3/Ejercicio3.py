months = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

while True:
    try:
        numero = int(input("Ingrese un numero del 1 al 12, correspondiendo a los meses del año: "))
        print(f"El mes numero {numero} es el mes de: {months[numero-1]}" )

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
    except IndexError:
        print("El número no corresponde a un mes del año")