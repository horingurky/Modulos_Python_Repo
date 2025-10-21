"""
Crea una jerarquía de clases para representar productos en una tienda. Debes implementar:

Una clase base Producto con los siguientes atributos y métodos:
Atributos: nombre, precio y stock
Un método mostrar_info() que devuelva un string con la información básica del producto
Un método hay_stock() que devuelva True si hay unidades disponibles
Una clase Alimento que herede de Producto y añada:
Un atributo adicional fecha_caducidad
Debe sobreescribir el método mostrar_info() para incluir la fecha de caducidad
Una clase Electronico que herede de Producto y añada:
Un atributo adicional garantia (en meses)
Debe sobreescribir el método mostrar_info() para incluir la información de garantía
Finalmente, crea una instancia de cada clase e imprime su información usando el método mostrar_info().

"""



print("=== PROGRAMA: JERARQUÍA DE PRODUCTOS ===\n")

# Clase base Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        # Inicializar atributos básicos
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def mostrar_info(self):
        # Devolver información básica del producto
        return f"El producto {self.nombre} con precio {self.precio} tiene un stock de {self.stock} artículos"
    
    def hay_stock(self):
        # Verificar si hay unidades disponibles
        return self.stock > 0
        
        

# Clase Alimento que hereda de Producto
class Alimento(Producto):
    def __init__(self, nombre, precio, stock, fecha_caducidad):
        # Llamar al constructor de la clase padre
        Producto.__init__(self, nombre, precio, stock)
        # Inicializar atributo específico de Alimento
        self.fecha_caducidad = fecha_caducidad
        
    
    def mostrar_info(self):
        # Sobreescribir el método para incluir fecha de caducidad
        # Escribe aquí tu código (puedes usar super() o reimplementar)
        


# Clase Electronico que hereda de Producto
class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, precio, stock)
        # Inicializar atributo específico de Electronico
        self.garantia = garantia
        
    
    def mostrar_info(self):
        # Sobreescribir el método para incluir información de garantía
        # Escribe aquí tu código (puedes usar super() o reimplementar)
        


# === CREACIÓN Y PRUEBA DE INSTANCIAS ===
print("=== CREANDO PRODUCTOS ===")

# Crear una instancia de Producto genérico
generico1 = Producto("television", 853, 12)


# Crear una instancia de Alimento
alimento1 = Alimento("tomates", 3.76, 123,"2025-10-29")

# Crear una instancia de Electronico
electronico1 = Electronico("Telefono", 389, 7, 36)

print("\n=== INFORMACIÓN DE PRODUCTOS ===")

# Mostrar información del producto genérico
# Escribe aquí tu código


# Mostrar información del alimento
# Escribe aquí tu código


# Mostrar información del electrónico
# Escribe aquí tu código


print("\n=== VERIFICANDO STOCK ===")

# Verificar stock de cada producto
# Escribe aquí tu código


