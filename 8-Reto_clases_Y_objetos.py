"""
        Constructor de la clase Libro
        
        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            paginas (int): Número total de páginas
        """
class Libro():

# def __init__....:
    def __init__(self,titulo,autor,paginas,disponible = True): # el True lo pone si no pones el parametro
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = disponible

# def devolver...
    def devolver(self):
        if self.disponible == False:
            self.disponible = True
            return (f"El libro {self.titulo} ha sido devuelto")
        else:
            return (f"El libro {self.titulo} NO está disponible")
        
    # def prestar...
    def prestar(self):
        if self.disponible == True:
            self.disponible = False
            return (f"El libro {self.titulo} ha sido prestado")
        else:
            return (f"El libro {self.titulo} no está disponible")
            
        
    # def informacion...
    def informacion(self):
        estado = f"Disponible" if self.disponible else "Prestado"
        return (f"Titulo: {self.titulo}\nAutor: {self.autor}\nNumero de pahinas: {self.paginas}\nEstado: {estado}")

            
                    


# Prueba de la clase Libro
def main():
    # Crear dos objetos libro diferentes
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)
    
    # Mostrar información inicial de los libros
    print("=== Información inicial de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())
    print("\n")
    
    # Prestar los libros
    print("=== Préstamo de libros ===")
    print(libro1.prestar())
    print(libro2.prestar())
    print("\n")
    
    # Intentar prestar un libro ya prestado
    print("=== Intento de préstamo de libros ya prestados ===")
    print(libro1.prestar())
    print("\n")
    
    # Mostrar información después del préstamo
    print("=== Información después del préstamo ===")
    print(libro1.informacion())
    print("\n")
    
    # Devolver un libro
    print("=== Devolución de libros ===")
    print(libro1.devolver())
    print("\n")
    
    # Intentar devolver un libro ya disponible
    print("=== Intento de devolución de libros ya disponibles ===")
    print(libro1.devolver())
    print("\n")
    
    # Mostrar información final
    print("=== Información final de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())



if __name__ == "__main__":
    main()
