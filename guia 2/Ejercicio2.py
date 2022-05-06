class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def print(self):
        if self.nota < 6:
            print("el alumno", self.nombre, "ha desaprobado con un ", self.nota)
        else:
            print("el alumno", self.nombre, "ha aprobado con un ", self.nota)


alumno1 = Alumno()
alumno1.__init__("fercho", 3)
alumno1.print()

alumno2 = Alumno()
alumno2.__init__("mono", 7)
alumno2.print()
