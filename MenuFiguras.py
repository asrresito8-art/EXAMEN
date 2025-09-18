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
def mostrar_menu(self):
        print(self.term.bold_purple(f"\n        Menú principal "))
        print(self.term.bold_blue(f"\n * Selecciona la figura deseada * "))
        print(self.term.bold__green("\n1. Rectángulo"))
        print(self.term.bold_blue("\n2. Cuadrado"))
        print(self.term.bold_pink("\n3. Círculo"))
        print(self.term.bold_orange("\n4. Triángulo"))
        print(self.term.bold_red("\n5. Salir"))
        
        opcion = input(self.term.bold_white("\nElige una opción: "))
        return opcion

def seleccionar_figura(self):
        while True:
            opcion = self.mostrar_menu()

            if opcion == "1":
                ancho = self.validar_float(self.term.green("\nIngrese el BASE del rectángulo: "))
                alto = self.validar_float(self.term.green("\nIngrese la ALTURA del rectángulo: "))
                rectangulo = Rectangulo(ancho, alto)
                self.mostrar_resultados(rectangulo)
