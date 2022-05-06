class Triangle:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def print(self):
        print("Lado A: ", self.ladoA)
        print("Lado B: ", self.ladoB)
        print("Lado C: ", self.ladoC)

    def higherOrLower(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            print("El lado A es el mas alto")
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            print("El lado B es el mas alto")
        elif self.ladoC > self.ladoA and self.ladoC > self.ladoB:
            print("El lado C es el mas alto")


triangle = Triangle()
triangle.__init__(3, 4, 5)
triangle.print()
triangle.higherOrLower()
