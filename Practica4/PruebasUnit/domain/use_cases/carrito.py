class Carrito:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        if precio < 0 or cantidad < 0:
            print("Error: No se pueden agregar productos con valores negativos.")
            return
        if precio > 100:
            precio = precio - precio*0.10
            print("Su producto tiene descuento.")
        producto = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        self.productos.append(producto)
        print(f"Producto '{nombre}' agregado al carrito.") 
    
    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto['nombre'] == nombre:
                self.productos.remove(producto)
                print(f"Producto '{nombre}' eliminado del carrito.")
                return
            
    def total_productos(self):
        print("Total productos:")
        for producto in self.productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
