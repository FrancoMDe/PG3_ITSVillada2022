list = [1,2,3,4,5,6,7,8,9,10]

num = int(input("Ingrese un numero: "))

def findIndex(lista, num):
    for i in lista:
        if num in lista:
            print(list.index(num)) 
            break
        else:
            print('el numero no esta en la lista')
            break

findIndex(list, num)