# DEFINO CLASE PRINCIPAL

class Persona:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

personas = []

def crear_persona():
    nombre = input("Ingrese el nombre: ")
    domicilio = input("Ingrese el domicilio: ")
    telefono = input("Ingrese el teléfono: ")
    email = input("Ingrese el email: ")
    dni = input("Ingrese el DNI: ")
    persona = Persona(nombre, domicilio, telefono, email, dni)
    personas.append(persona)
    print("¡Persona agregada!")

def leer_personas():
    if not personas:
        print("No hay personas disponibles.")
    for persona in personas:
        #    print(f"Nombre: {persona.nombre}, 
        #        Domicilio: {persona.domicilio},
        #        Teléfono: {persona.telefono}, 
        #        Email: {persona.email}")
        print("Nombre:",persona.nombre, 
              " Domicilio:",persona.domicilio,
              " Teléfono:",persona.telefono, 
              "Email:",persona.email,
              "DNI",persona.dni)

def actualizar_persona():
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

def borrar_persona():
    nombre = input("Ingrese el nombre de la persona a borrar: ")
    global personas
    personas = [persona for persona in personas if persona.nombre != nombre]
    print("¡Persona borrada!")

def menu():
    while True:
        print("\nMenú de Personas")
        print("1. Crear persona")
        print("2. Leer personas")
        print("3. Actualizar persona")
        print("4. Borrar persona")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_persona()
        elif opcion == "2":
            leer_personas()
        elif opcion == "3":
            actualizar_persona()
        elif opcion == "4":
            borrar_persona()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
menu()

