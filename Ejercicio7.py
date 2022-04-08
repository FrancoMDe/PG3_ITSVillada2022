number = str(input("Ingrese un numero: "))
contador = 0



def stepNumber(number):
    isStep = True
    for i in range(len(number)-1):
        if int(number[i]) - int(number[i+1]) != 1 and int(number[i]) - int(number[i+1]) != -1:
            print("El numero ingresado no es un step")
            isStep = False
            break
    if isStep:
            print("El numero ingresado es un step")

stepNumber(number)