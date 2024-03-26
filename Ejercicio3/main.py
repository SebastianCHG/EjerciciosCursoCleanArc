from Animal import *


miPerro = Perro("Tony")
miVaca = Vaca("Lola")

print(miPerro.nombre + " " + miPerro.comer())
print(miVaca.nombre + " " + miVaca.comer())

print(miPerro.nombre + " " + miPerro.respirar())
print(miVaca.nombre + " " + miVaca.respirar())


print(miPerro.nombre + " " + miPerro.dormir())
print(miVaca.nombre + " " + miVaca.dormir())


print(miPerro.nombre + " " + miPerro.cazar())
print(miVaca.nombre + " " + miVaca.pastar())

#print(miPerro.pastar())  //No es un animal que paste