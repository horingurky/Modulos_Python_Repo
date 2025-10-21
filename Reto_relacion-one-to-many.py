"""
Crea un sistema de gestión de carpetas y archivos que implemente una relación one-to-many en Python.

Pasos a realizar:
Crear la clase Carpeta con los siguientes atributos:

id: identificador único (entero)
nombre: nombre de la carpeta (cadena)
fecha_creacion: fecha de creación (cadena)
archivos: lista de archivos (inicializar como lista vacía)
Crear la clase Archivo con los siguientes atributos:

id: identificador único (entero)
nombre: nombre del archivo (cadena)
extension: extensión del archivo (cadena)
tamaño: tamaño en bytes (entero)
carpeta_id: ID de la carpeta propietaria (entero)
Crear objetos:

Una carpeta: con id: 1, nombre: Proyecto Aviberico, fecha de creación: 2025-01-15
Tres archivos:
id: 1, nombre: main, extensión: py, tamaño: 1024, id de carpeta: 1
id: 2, nombre: config, extensión: json, tamaño: 512, id de carpeta: 1
id: 3, nombre: readme, extensión: md, tamaño: 256, id de carpeta: 1
Establecer la relación one-to-many:

Agregar los archivos a la carpeta
Verificar que una carpeta puede tener múltiples archivos y cada archivo pertenece a una sola carpeta
Mostrar la información de la carpeta y sus archivos, confirmando que la relación funciona correctamente.

"""





print("=== EJERCICIO: RELACIÓN CARPETA-ARCHIVOS ===\n")

# 1. Crear la clase Carpeta con los atributos: id, nombre, fecha_creacion
# El atributo 'archivos' debe inicializarse como una lista vacía
class Carpeta:
    def __init__(self, id, nombre, fecha_creacion):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = fecha_creación
        self.archivos = []


# 2. Crear la clase Archivo con los atributos: id, nombre, extension, tamaño, carpeta_id
class Archivo:
    def __init__(self, id, nombre, extension, tamaño, carpeta_id):
        # Escribe aquí tu código

print("=== CREANDO OBJETOS ===")

# 3. Crear una carpeta con id: 1, nombre: Proyecto Aviberico, fecha de creación: 2025-01-15


# 4. Crear tres archivos:
# - id: 1, nombre: main, extensión: py, tamaño: 1024, id de carpeta: 1
# - id: 2, nombre: config, extensión: json, tamaño: 512, id de carpeta: 1
# - id: 3, nombre: readme, extensión: md, tamaño: 256, id de carpeta: 1


print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Agregar los archivos a la carpeta (relación one-to-many)


print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información de la carpeta y sus archivos
# Hay que mostrar:
# - Nombre de la carpeta
# - Número total de archivos
# - Lista de archivos con sus detalles

print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación one-to-many