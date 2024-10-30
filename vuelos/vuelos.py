class Vuelo:
    def __init__(self, idvuelo, aerolinea, estado, observaciones, destino):
        self.idvuelo = idvuelo
        self.aerolinea = aerolinea
        self.estado = estado
        self.observaciones = observaciones
        self.destino = destino

vuelos = []

def crear_vuelo():
    idvuelo = input("Ingrese el ID del vuelo: ")
    aerolinea = input("Ingrese la aerolínea: ")
    estado = input("Ingrese el estado: ")
    observaciones = input("Ingrese observaciones: ")
    destino = input("Ingrese el destino: ")
    vuelo = Vuelo(idvuelo, aerolinea, estado, observaciones, destino)
    vuelos.append(vuelo)
    print("¡Vuelo agregado!")

def leer_vuelos():
    if not vuelos:
        print("No hay vuelos disponibles.")
    for vuelo in vuelos:
        print(f"ID: {vuelo.idvuelo}, Aerolínea: {vuelo.aerolinea}, Estado: {vuelo.estado}, Observaciones: {vuelo.observaciones}, Destino: {vuelo.destino}")

def actualizar_vuelo():
    idvuelo = input("Ingrese el ID del vuelo a actualizar: ")
    for vuelo in vuelos:
        if vuelo.idvuelo == idvuelo:
            vuelo.aerolinea = input("Ingrese la nueva aerolínea: ")
            vuelo.estado = input("Ingrese el nuevo estado: ")
            vuelo.observaciones = input("Ingrese las nuevas observaciones: ")
            vuelo.destino = input("Ingrese el nuevo destino: ")
            print("¡Vuelo actualizado!")
            return
    print("Vuelo no encontrado.")

def borrar_vuelo():
    idvuelo = input("Ingrese el ID del vuelo a borrar: ")
    global vuelos
    vuelos = [vuelo for vuelo in vuelos if vuelo.idvuelo != idvuelo]
    print("¡Vuelo borrado!")

def menu():
    while True:
        print("\nMenú de Vuelos")
        print("1. Crear vuelo")
        print("2. Leer vuelos")
        print("3. Actualizar vuelo")
        print("4. Borrar vuelo")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_vuelo()
        elif opcion == "2":
            leer_vuelos()
        elif opcion == "3":
            actualizar_vuelo()
        elif opcion == "4":
            borrar_vuelo()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
            
menu()
