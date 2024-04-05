from abc import ABC,  abstractmethod

class BaseDatos(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def guardar(self, datos):
        pass
    
    @abstractmethod
    def leer(self):
        pass