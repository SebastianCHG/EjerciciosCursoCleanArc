import mysql.connector
from BaseDatos import *

class MySQL(BaseDatos):

    def __init__(self) -> None:
        pass

    def guardar(self, datos):
        print("Se guarda los datos " + datos + " en la BD mySQL")

    def leer(self):
        print("Se lee en la BD my SQL")