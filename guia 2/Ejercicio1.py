class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def print(self):
        print("nombre: ", self.nombre)


persona1 = Persona()
persona1.__init__("Franco")
persona1.print()

persona2 = Persona()
persona2.__init__("Jose")
persona2.print()
