# DEFINO CLASE PRINCIPAL

# Contactos
# Nombre
# Telefono
# Email

class Consorcista:
    def __init__(self, nombre, unidad):
        self.nombre = nombre
        self.unidad = unidad

consorcistas = []

def Crear_consorcista():
    nombre = input("Ingrese el nombre del consorcista: ")
    unidad = input("Ingrese el codigo de la unidad: ")

    consorcista = Consorcista(nombre, unidad)
    consorcistas.append(consorcista)
    print("¡El Consorcista fué agregado!")

def Leer_consorcistas():
    if not consorcistas:
        print("No hay disponibles.")
    for consorcista in consorcistas:
        #    print(f"Nombre: {persona.nombre}, 
        #        Domicilio: {persona.domicilio},
        #        Teléfono: {persona.telefono}, 
        #        Email: {persona.email}")
        print("Nombre:",consorcista.nombre, 
              " Unidad: ",consorcista.unidad)

def Actualizar_consorcista():
    nombre = input("Ingrese el nombre del consorcista a actualizar: ")
    for consorcista in consorcistas:
        if consorcista.nombre == nombre:
            consorcista.unidad = input("Ingrese la nueva unidad: ")
            print("¡Consorcista actualizado!")
            return
    print("No esta ese consorcista.")

def Borrar_persona():
    nombre = input("Ingrese el nombre del Consorcita a borrar: ")
    global consorcistas
    consorcistas = [consorcista for consorcista in consorcistas if consorcista.nombre != nombre]
    print("¡Consorcista eliminado!")

def Menu():
    while True:
        print("\nMenú de Consorcistas")
        print("1. Crear Consorcista")
        print("2. Leer Consorcistas")
        print("3. Actualizar Consorcista")
        print("4. Borrar Consorcista")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Crear_consorcista()
        elif opcion == "2":
            Leer_consorcistas()
        elif opcion == "3":
            Actualizar_consorcista()
        elif opcion == "4":
            Borrar_persona()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
Menu()

