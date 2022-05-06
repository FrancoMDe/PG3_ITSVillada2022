width = int(input("Ingrese el ancho de la figura: "))
height = int(input("Ingrese el alto de la figura: "))
character = input("Ingrese el caracter de la figura: ")


def rectangle(width, height, character):
    for i in range(height):
        for j in range(width):
            print(character, end="")
        print()


rectangle(width, height, character)
