class Cuadrado:
    def __init__(self, lado: float):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado
