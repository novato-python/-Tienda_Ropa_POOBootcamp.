class Prenda:
    def __init__(self, tipo, precio, cantidad):
        self.tipo = tipo
        self.precio = precio
        self.cantidad = cantidad
    
    def mostrar_info(self):
        print(f"Tipo de prenda: {self.tipo}, Precio: {self.precio}, Cantidad: {self.cantidad}")
    
class RopaHombre(Prenda):
    def __init__(self, tipo, precio, cantidad, talla):
        super().__init__(tipo, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        print(f"Tipo de prenda: {self.tipo}, Precio: {self.precio}, Cantidad: {self.cantidad}, Talla: {self.talla}")

class RopaMujer(Prenda):
    def __init__(self, tipo, precio, cantidad, talla):
        super().__init__(tipo, precio, cantidad)
        self.talla = talla
    
    def mostrar_info(self):
        print(f"Tipo de prenda: {self.tipo}, Precio: {self.precio}, Stock: {self.cantidad}, Talla: {self.talla}")

class Inventario:
    def __init__(self):
        self.prendas = []  

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda) 

    def mostrar_inventario(self):
        for indice, prenda in enumerate(self.prendas, start=1):
            print(f"{indice}. ", end="")
            prenda.mostrar_info()
            
class Tienda:
    def __init__(self):
        self.inventario = Inventario()  
    
    def agregar_prenda(self, prenda):
        self.inventario.agregar_prenda(prenda) 
    
    def mostrar_inventario(self):
        print("Inventario de la tienda:")
        self.inventario.mostrar_inventario()  
    
    def comprar_producto(self, tipo, cantidad):
        for prenda in self.inventario.prendas:
            if prenda.tipo == tipo:
                if prenda.cantidad >= cantidad:
                    prenda.cantidad -= cantidad
                    print(f"Compra realizada: {cantidad} {prenda.tipo}(s) por ${prenda.precio * cantidad:.2f}")
                    return
                else:
                    print(f"No hay suficiente stock de {tipo}. Stock disponible: {prenda.cantidad}")
                    return
        print(f"No se encontró el producto: {tipo}")

class Carrito:
    def __init__(self):
        self.productos = []
        
    def agregar_productos(self, prenda, cantidad):
        self.productos.append((prenda, cantidad))  # Guardamos la prenda y la cantidad
    
    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito está vacío")
            return
        for prenda, cantidad in self.productos:  
            print(f"{prenda.tipo} - Cantidad: {cantidad}, Precio Unitario: ${prenda.precio:.2f}, Total: ${prenda.precio * cantidad:.2f}")
    
    def vaciar_carrito(self):
        self.productos = []
    
    def confirmar_compra(self):
        print("Confirmando compra...")
        total = 0
        for prenda, cantidad in self.productos:
            if prenda.cantidad >= cantidad:
                prenda.cantidad -= cantidad
                total += prenda.precio * cantidad
            else:
                print(f"No hay suficiente stock para {prenda.tipo}. Stock disponible: {prenda.cantidad}")
                continue
        print(f"Compra confirmada. Total a pagar: ${total:.2f}")
        self.vaciar_carrito()  # Cambié self.carrito a self

# Crear el inventario y agregar prendas
inventario = Inventario()
inventario.agregar_prenda(RopaHombre("Camisa de Hombre", 25.00, 50, 'M'))
inventario.agregar_prenda(RopaHombre("Pantalón de Hombre", 30.00, 30, 'P'))
inventario.agregar_prenda(RopaHombre("Chaqueta de Hombre", 55.00, 20, 'G'))
inventario.agregar_prenda(RopaHombre("Zapatos de Hombre", 60.00, 25, 'P'))
inventario.agregar_prenda(RopaMujer("Falda de Mujer", 28.00, 15, 'M'))
inventario.agregar_prenda(RopaMujer("Blusa de Mujer", 22.00, 40, 'P'))
inventario.agregar_prenda(RopaMujer("Vestido de Mujer", 45.00, 10, 'G'))
inventario.agregar_prenda(RopaMujer("Zapatos de Mujer", 50.00, 20, 'XP'))

tienda = Tienda()
for prenda in inventario.prendas:
    tienda.agregar_prenda(prenda)

carrito = Carrito()

while True:
    print("\nMenu del carrito:")
    print("1. Agregar prenda al carrito")
    print("2. Mostrar carrito")
    print("3. Vaciar carrito")
    print("4. Confirmar compra")
    print("5. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        tienda.mostrar_inventario()
        indice = int(input("Seleccione la prenda que desea agregar al carrito (1-{}): ".format(len(tienda.inventario.prendas)))) - 1
        
        if indice>=0 and indice<len(inventario.prendas):
            prenda_encontrada = inventario.prendas[indice]
            cantidad = int(input("Seleccione la cantidad que desea agregar al carrito: "))
          
            if cantidad > prenda_encontrada.cantidad:
                print(f"No hay suficiente stock de {prenda_encontrada.tipo}. Stock disponible: {prenda_encontrada.cantidad}")
            else:
                carrito.agregar_productos(prenda_encontrada, cantidad)
    
    elif opcion == 2:
        print("---Carrito Actual---")
        carrito.mostrar_carrito()
    elif opcion == 3:
        carrito.vaciar_carrito()
        print("---El carrito a sido vaciado---")
    elif opcion == 4:
        carrito.confirmar_compra()
    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
