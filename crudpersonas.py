
# DEFINO CLASE PRINCIPAL

class Persona:
    def __init__(self, nombre, domicilio, telefono, email, dni):
        self.nombre = nombre
        self.domicilio = domicilio
        self.telefono = telefono
        self.email = email
        self.dni = dni

personas = []

def Crear_persona():
    nombre = input("Ingrese el nombre: ")
    domicilio = input("Ingrese el domicilio: ")
    telefono = input("Ingrese el teléfono: ")
    email = input("Ingrese el email: ")
    dni = input("Ingrese el DNI: ")
    persona = Persona(nombre, domicilio, telefono, email, dni)
    personas.append(persona)
    print("¡Persona agregada!")

def Leer_personas():
    if not personas:
        print("No hay personas disponibles.")
    for persona in personas:
        print("Nombre:",persona.nombre, 
              " Domicilio:",persona.domicilio,
              " Teléfono:",persona.telefono, 
              "Email:",persona.email,
              "DNI",persona.dni)

def Actualizar_persona():
    nombre = input("Ingrese el nombre de la persona a actualizar: ")
    for persona in personas:
        if persona.nombre == nombre:
            persona.domicilio = input("Ingrese el nuevo domicilio: ")
            persona.telefono = input("Ingrese el nuevo teléfono: ")
            persona.email = input("Ingrese el nuevo email: ")
            persona.dni = input("Ingrese el nuevo DNI: ")
            print("¡Persona actualizada!")
            return
    print("Persona no encontrada.")

def Borrar_persona():
    nombre = input("Ingrese el nombre de la persona a borrar: ")
    global personas
    personas = [persona for persona in personas 
                if persona.nombre != nombre]
    print("¡Persona borrada!")

def Menu():
    while True:
        print("\nMenú de Personas")
        print("1. Crear persona")
        print("2. Leer personas")
        print("3. Actualizar persona")
        print("4. Borrar persona")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Crear_persona()
        elif opcion == "2":
            Leer_personas()
        elif opcion == "3":
            Actualizar_persona()
        elif opcion == "4":
            Borrar_persona()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
Menu()

