from Figura import *
from Rectangulo import *
from Cuadrado import *

miFigura = Figura()
miRectangulo = Rectangulo(6,4)
miCuadrado = Cuadrado(5)

vector = []

vector.append(miRectangulo)
vector.append(miCuadrado)
vector.append("Nada")

#print(miRectangulo.area())
#print(miRectangulo.perimetro())
#print(miCuadrado.area())
#print(miCuadrado.perimetro())

print(vector[0].area())
print(vector[1].area())
print(vector[2])