
class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.abierto = False
    
    def abrir(self):
        self.abierto = True
        print(f"el libro {self.titulo} se ha abierto")

    def cerrar(self):
        self.abierto = False
        print(f"el libro {self.titulo} se ha cerrado")

# Definición de la clase

class Producto:
    def __init__(self, nombre, precio, stock = 0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

# Crear objetos producto

laptop = Producto("ordenador barato",350) # El stock será 0 (porque el valor por defecto es 0).

teclado = Producto("Teclado mecánico", 80, 15) # El stock ahora es 15.

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto
        self.perimetro = 2 * (ancho + alto)

rectangulo = Rectangulo(3, 5)
