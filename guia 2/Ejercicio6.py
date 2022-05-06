class Familia:
    def __init__(self):
        self.padre = str(input("Ingrese el nombre del padre: "))
        self.madre = str(input("Ingrese el nombre de la madre: "))
        self.hijos = []
        cantHijos = int(input("Ingrese la cantidad de hijos: "))
        for i in range(cantHijos):
            self.hijos.append(str(input("Ingrese el nombre del hijo/hija: ")))

    def __str__(self):
        return (
            "Padre: "
            + self.padre
            + "\nMadre: "
            + self.madre
            + "\nHijos: "
            + str(self.hijos)
        )


familia = Familia()
print(familia)
