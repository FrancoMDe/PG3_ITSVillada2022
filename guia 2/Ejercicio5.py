class Persona:
    def __init__(self):
        self.nombre = str(input("Ingrese su nombre: "))
        self.edad = int(input("Ingrese su edad: "))
        self.imprimir()

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)


persona = Persona()


class Empleado(Persona):
    def __init__(self, sueldo):
        self.sueldo = int(input("Ingrese su sueldo: "))
        self.imprimir()
        self.impuestos()

    def impuestos(self):
        if self.sueldo > 3000:
            print("Tiene que pagar impuestos")
        else:
            print("No tiene que pagar impuestos")

    def imprimir(self):
        print("Sueldo: ", self.sueldo)


empleado = Empleado(0)
