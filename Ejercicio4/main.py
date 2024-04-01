from ManejadorDatos import *
from MongoDB import *
from MySQL import *

miManejador = ManejadorDatos()
miSQL = MySQL()
miMongo = MongoDB()

datos = input("Ingrese los datos a guardar: ")

ManejadorDatos.procesarLeer(miSQL)
ManejadorDatos.procesarLeer(miMongo)
ManejadorDatos.procesarGuardar(miSQL, datos)
ManejadorDatos.procesarGuardar(miMongo, datos)