from Calculadora import *

x1 = int(input("Inserte el primer número "))
x2 = int(input("Inserte el segundo número "))

miCalculadora = Calculadora(x1,x2)

miCalculadora.sumar()
miCalculadora.restar()
miCalculadora.multiplicar()
miCalculadora.dividir()
