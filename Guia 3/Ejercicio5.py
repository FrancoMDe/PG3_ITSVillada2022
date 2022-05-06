texto = open("texto.txt", "w")
texto.write("Hola, esto es una prueba")
try:
    texto.write(8)
except TypeError:
    print("Error: No se puede escribir un número, solo se permiten strings")    