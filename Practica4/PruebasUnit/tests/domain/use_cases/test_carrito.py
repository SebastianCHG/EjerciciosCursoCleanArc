import pytest
from domain.use_cases.carrito import Carrito

def setUp(self):
        self.carrito = Carrito()

def test_agregar_producto():
    carrito = Carrito()
    carrito.agregar_producto("aceite",40,1)
    assert carrito.productos[0]['nombre'] == "aceite"
    assert carrito.productos[0]['precio'] == 40
    assert carrito.productos[0]['cantidad'] == 1

def test_total_productos():
    carrito = Carrito()
    carrito.agregar_producto("azucar",40,1)
    carrito.agregar_producto("galletas",50,1)
    assert len(carrito.productos) == 2

def  test_eliminar_producto():
    carrito = Carrito()
    carrito.agregar_producto("azucar",40,2)
    carrito.agregar_producto("arroz",25,1)
    carrito.eliminar_producto("azucar")
    assert not [productos['nombre'] for productos in carrito.productos] == "azucar"

def test_agregar_producto_precio_negativo():
    carrito = Carrito()
    carrito.agregar_producto("azucar",-40,1)
    assert carrito.productos[0]['nombre'] == "azucar"
    assert carrito.productos[0]['precio'] == -40
    assert carrito.productos[0]['cantidad'] == 1