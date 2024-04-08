Feature: Agregar producto al carrito con descuento
    As un comprador
    I quiero obtener un descuento
    So ahorrar dinero

  Scenario: Agregar producto con precio mayor a 100
    Given que tengo un carrito vacio
    When agrego un producto arroz con precio 150 y cantidad 1
    Then el producto debe tener un descuento y su costo es de 135.0