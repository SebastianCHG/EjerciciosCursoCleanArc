import pymongo
from BaseDatos import *

class MongoDB(BaseDatos):

    def __init__(self) -> None:
        super().__init__()

    def guardar(self, datos):
        print("Se guarda los datos " + datos + " en la MongoDB")
    
    def leer(self):
        print("Se lee en la MongoDB")