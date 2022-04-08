phrase = input(str("Ingrese una frase: "))

def countVowels(phrase):
    contador = 0
    for i in phrase:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            contador += 1
    if contador > 0:
        print("La frase tiene " + str(contador) + " vocales")
    else:
        print("La frase no tiene vocales")    

countVowels(phrase)