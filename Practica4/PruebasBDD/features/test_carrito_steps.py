from pytest_bdd import scenario, given, when, then
from carrito import Carrito

carrito = Carrito()

@scenario('test_carrito.feature', 'Agregar producto con precio mayor a 100')
def test_precio_mayor():
    pass

@given('que tengo un carrito vacio')
def carrito_vacio():
    return carrito

@when('agrego un producto arroz con precio 150 y cantidad 1')
def agregar_producto_carrito():
    carrito_vacio().agregar_producto("arroz", 150, 1)

@then('el producto debe tener un descuento y su costo es de 135.0')
def producto_descuento():
    print(carrito.productos[0]['precio'])
    assert carrito.productos[0]['precio'] == 135.0