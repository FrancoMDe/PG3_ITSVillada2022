word = input("Ingrese una palabra: ")

def palindrome(word):
    if word == word[::-1]:
        print("La palabra " + word + " es capicua")
    else:
        print("La palabra " + word + " no es capicua")     

palindrome(word)