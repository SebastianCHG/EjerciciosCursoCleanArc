from abc import ABC,  abstractmethod

class Animal(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    def respirar(self):
        return "está respirando"

    @abstractmethod
    def comer(self):
        pass
    
    def dormir(self):
        return "está dumiendo"
    
    def getNombre(self):
        return self.nombre


class Carnivoro(Animal):

    def __init__(self, nombre):
        super().__init__(nombre)

    def respirar(self):
        return super().respirar()
    
    def comer(self):
        return "está comiendo carne"
    
    @abstractmethod
    def cazar(self):
        pass
    
    def dormir(self):
        return super().dormir()


class Herbivoro(Animal):

    def __init__(self, nombre):
        super().__init__(nombre)

    def respirar(self):
        return super().respirar()
    
    def comer(self):
        return "está comiendo hierbas"
    
    @abstractmethod
    def pastar(self):
        pass
    
    def dormir(self):
        return super().dormir()
    
class Perro(Carnivoro):

    def __init__(self, nombre):
        super().__init__(nombre)

    def cazar(self):
        return "el perro está cazando"

class Vaca(Herbivoro):

    def __init__(self, nombre):
        super().__init__(nombre)

    def pastar(self):
        return "la vaca está pastando"