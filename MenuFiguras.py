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
        print(self.term.bold_green(f"\n1. Rectángulo"))
        print(self.term.bold_blue(f"\n2. Cuadrado"))
        print(self.term.bold_pink(f"\n3. Círculo"))
        print(self.term.bold_orange(f"\n4. Triángulo"))
        print(self.term.bold_red(f"\n5. Salir"))
        
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
            
            elif opcion == "2":
                lado = self.validar_float("       Ingrese un LADO del cuadrado: ")
                cuadrado = Cuadrado(lado)
                self.mostrar_resultados(cuadrado)
               
            elif opcion == "3":
                radio = self.validar_float("      Ingrese el RADIO del círculo: ")
                circulo = Circulo(radio)
                self.mostrar_resultados(circulo)

            elif opcion == "4":
                base = self.validar_float(  "Ingrese la BASE del triángulo:  ")
                altura = self.validar_float("Ingrese la ALTURA del triángulo:")
                lado1 = self.validar_float( "Ingrese el   LADO1 del triángulo:  ")
                lado2 = self.validar_float( "Ingrese el   LADO2 del triángulo:  ")
                triangulo = Triangulo(base, altura, lado1, lado2)
                self.mostrar_resultados(triangulo)

            elif opcion == "5":
                print(self.term.bold_blue2("¡Gracias por usar el programa!"))
                break

            else:
                print(self.term.red("Opción no válida. Inténtalo nuevamente."))
            
    def mostrar_resultados(self, figura):
        print(self.term.bold_cyan(f"\nResultados para {figura.__class__.__name__}:"))
        print(self.term.green3(f"Área: {figura.area():.2f}"))
        print(self.term.green3(f"Perímetro: {figura.perimetro():.2f}\n"))

if __name__ == "__main__":
    menu = MenuFiguras()
    menu.seleccionar_figura()
