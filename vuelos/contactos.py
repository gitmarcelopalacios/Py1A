class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

contactos = []

def crear_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el teléfono del contacto: ")
    email = input("Ingrese el correo electrónico del contacto: ")
    contacto = Contacto(nombre, telefono, email)
    contactos.append(contacto)
    print("¡Contacto agregado!")

def leer_contactos():
    if not contactos:
        print("No hay contactos disponibles.")
    for contacto in contactos:
        print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")

def actualizar_contacto():
    nombre = input("Ingrese el nombre del contacto a actualizar: ")
    for contacto in contactos:
        if contacto.nombre == nombre:
            contacto.telefono = input("Ingrese el nuevo teléfono: ")
            contacto.email = input("Ingrese el nuevo correo electrónico: ")
            print("¡Contacto actualizado!")
            return
    print("Contacto no encontrado.")

def borrar_contacto():
    nombre = input("Ingrese el nombre del contacto a borrar: ")
    global contactos
    contactos = [contacto for contacto in contactos if contacto.nombre != nombre]
    print("¡Contacto borrado!")

def menu():
    while True:
        print("\nMenú de Contactos")
        print("1. Crear contacto")
        print("2. Leer contactos")
        print("3. Actualizar contacto")
        print("4. Borrar contacto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_contacto()
        elif opcion == "2":
            leer_contactos()
        elif opcion == "3":
            actualizar_contacto()
        elif opcion == "4":
            borrar_contacto()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

menu()
