from Figura import *

class Rectangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return "El área del rectángulo es " + str(self.base * self.altura)
    
    def perimetro(self):
        return "El perímetro del rectángulo es " + str((self.base + self.altura)*2)