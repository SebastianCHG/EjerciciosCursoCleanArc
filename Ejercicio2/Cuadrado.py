from Figura import *

class Cuadrado(Figura):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return "El área del cuadrado es " + str(self.lado ** 2)
    
    def perimetro(self):
        return "El perímetro del cuadrado es " + str(self.lado * 4)