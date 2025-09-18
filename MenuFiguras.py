from Figuras import Rectangulo, Cuadrado, Circulo, Triangulo #se importa de nuestro archivo las formulas de las figuras 

from blessed import Terminal # para ocupar los colores 

class MenuFiguras: # se empieza el codigo
    def __init__(self):
        self.term = Terminal()

    def validar_float(self, mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                if valor <= 0:
                    print(self.term.blod_red("¡Error! El valor debe ser mayor que 0 y menor a 5."))
                else:
                    return valor
            except ValueError:
                print(self.term.blod_red("¡Error! Debe ingresar un valor asignado."))
