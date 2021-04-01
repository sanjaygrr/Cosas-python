
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == "__main__":
    rectangulo = Rectangulo(base = int(input('indique la base del rectangulo')) , altura = int(input('indique la altura del rectangulo')))
    print('El area del rectangulo es: ' + rectangulo.area())

    cuadrado = Cuadrado(lado = int(input('ingrese el lado del cuadrado')))
    print('El area del cuadrado es ' + cuadrado.area())