class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.printNumeros()
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        suma = self.num1 + self.num2
        print("suma: ", suma)

    def restar(self):
        resta = self.num1 - self.num2
        print("resta: ", resta)

    def multiplicar(self):
        multiplicacion = self.num1 * self.num2
        print("multiplicacion: ", multiplicacion)

    def dividir(self):
        division = self.num1 / self.num2
        print("division: ", division)

    def printNumeros(self):
        print("primer numero: ", self.num1)
        print("segundo numero: ", self.num2)


numeros = Operaciones(10, 5)
