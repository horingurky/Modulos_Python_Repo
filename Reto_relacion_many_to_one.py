"""
https://app.certidevs.com/code-exam-score/77f1c938-c5ea-425e-b0ee-9d0ee68961ce

Crea un sistema de gestión hotelera que implemente una relación many-to-one en Python.

Pasos a realizar:
Crear la clase Hotel con los siguientes atributos:

id: identificador único (entero)
nombre: nombre del hotel (cadena)
direccion: dirección del hotel (cadena)
estrellas: número de estrellas (entero)
Crear la clase Habitacion con los siguientes atributos:

id: identificador único (entero)
numero: número de la habitación (entero)
tipo: tipo de habitación (cadena)
precio: precio por noche (entero)
hotel: objeto hotel al que pertenece la habitación
Crear objetos:

Un hotel: con id: 1, nombre: Hotel Carbonero, dirección: Plaza Parus Mayor 123, estrellas: 4
Tres habitaciones:
id: 1, número: 101, tipo: Individual, precio: 80, hotel: Hotel Carbonero
id: 2, número: 102, tipo: Doble, precio: 120, hotel: Hotel Carbonero
id: 3, número: 103, tipo: Suite, precio: 200, hotel: Hotel Carbonero

Mostrar la información del hotel y sus habitaciones, confirmando que la relación funciona correctamente.


"""





print("=== EJERCICIO: RELACIÓN HABITACIONES-HOTEL ===\n")

# 1. Crear la clase Hotel con los atributos: id, nombre, direccion, estrellas
class Hotel:
    def __init__(self, id, nombre, direccion, estrellas):
        # Escribe aquí tu código

# 2. Crear la clase Habitacion con los atributos: id, numero, tipo, precio, hotel
class Habitacion:
    def __init__(self, id, numero, tipo, precio, hotel):
        # Escribe aquí tu código

print("=== CREANDO OBJETOS ===")

# 3. Crear un hotel con id: 1, nombre: Hotel Carbonero, dirección: Plaza Parus Mayor 123, estrellas: 4


# 4. Crear tres habitaciones:
# - id: 1, número: 101, tipo: Individual, precio: 80, hotel: Hotel Carbonero
# - id: 2, número: 102, tipo: Doble, precio: 120, hotel: Hotel Carbonero
# - id: 3, número: 103, tipo: Suite, precio: 200, hotel: Hotel Carbonero


print("=== VERIFICANDO RELACIÓN ===")

# 5. Imprimir información del hotel y sus habitaciones
# Hay que mostrar:
# - Nombre del hotel y sus estrellas

print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación many-to-one