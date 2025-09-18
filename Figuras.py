class Cuadrado:
    def __init__(self, lado: float):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado
    
class Rectangulo:
    def __init__(self, ancho: float, alto: float): 
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)
