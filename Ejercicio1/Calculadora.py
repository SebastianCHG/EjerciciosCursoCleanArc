class Calculadora:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def escribirResultado(self, resultado):
        print(resultado)

    def sumar(self): 
        self.escribirResultado(self.numero1 + self.numero2)
    
    def restar(self):
        self.escribirResultado(self.numero1 - self.numero2)
    
    def multiplicar(self):
        self.escribirResultado(self.numero1 * self.numero2)
    
    def dividir(self):
        self.escribirResultado(self.numero1 / self.numero2)

    