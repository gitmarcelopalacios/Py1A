



# DEFINO CLASE PRINCIPAL

class Limite:
    def __init__(self, nombre, limite_credito):
        self.nombre = nombre
        self.limite_credito = limite_credito


limites = []

def Crear():
    nombre = input("Ingrese el nombre: ")
    limite_credito = input("Ingrese el limite_credito: ")
    limite = Limite(nombre, limite_credito)
    limites.append(limite)
    print("¡Persona agregada!")

def Leer():
    if not limites:
        print("No hay limites de credito disponibles.")
    for limite in limites:
        print("Nombre:",limite.nombre, 
              " Limite de credito:",limite.limite_credito)


def Actualizar():
    nombre = input("Ingrese el nombre de la persona a actualizar: ")
    for limite in limites:
        if limite.nombre == nombre:
            limite.limite_credito = input("Ingrese el nuevo limite de credito: ")
            print("¡Limite actualizada!")
            return
    print("limite no encontrado.")

def Borrar():
    nombre = input("Ingrese el nombre de la persona a borrar: ")
    global limites
    limites = [limite for limite in limites 
                if limite.nombre != nombre]
    print("¡Limite borrado!")

def Menu():
    while True:
        print("\nMenú ")
        print("1. Crear")
        print("2. Leer")
        print("3. Actualizar")
        print("4. Borrar")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Crear()
        elif opcion == "2":
            Leer()
        elif opcion == "3":
            Actualizar()
        elif opcion == "4":
            Borrar()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
Menu()

