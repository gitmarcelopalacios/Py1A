import json

class Vuelo:
    def __init__(self, aerolinea, hora_llegada, codigo_vuelo, origen, estado, terminal, puerta):
        self.aerolinea = aerolinea
        self.hora_llegada = hora_llegada
        self.codigo_vuelo = codigo_vuelo
        self.origen = origen
        self.estado = estado
        self.terminal = terminal
        self.puerta = puerta

    def to_dict(self):
        return {
            'aerolinea': self.aerolinea,
            'hora_llegada': self.hora_llegada,
            'codigo_vuelo': self.codigo_vuelo,
            'origen': self.origen,
            'estado': self.estado,
            'terminal': self.terminal,
            'puerta': self.puerta
        }

vuelos = []

def guardar_vuelos():
    with open('vuelos.json', 'w') as file:
        json.dump([vuelo.to_dict() for vuelo in vuelos], file)

def cargar_vuelos():
    global vuelos
    try:
        with open('vuelos.json', 'r') as file:
            vuelos = [Vuelo(**data) for data in json.load(file)]
    except FileNotFoundError:
        vuelos = []

def crear_vuelo():
    aerolinea = input("Ingrese la aerolínea: ")
    hora_llegada = input("Ingrese la hora de llegada: ")
    codigo_vuelo = input("Ingrese el código de vuelo: ")
    origen = input("Ingrese el origen: ")
    estado = input("Ingrese el estado: ")
    terminal = input("Ingrese la terminal: ")
    puerta = input("Ingrese la puerta: ")
    vuelo = Vuelo(aerolinea, hora_llegada, codigo_vuelo, origen, estado, terminal, puerta)
    vuelos.append(vuelo)
    guardar_vuelos()
    print("¡Vuelo agregado!")

def leer_vuelos():
    if not vuelos:
        print("No hay vuelos disponibles.")
    for vuelo in vuelos:
        print(f"Aerolínea: {vuelo.aerolinea}, Hora de llegada: {vuelo.hora_llegada}, Código de vuelo: {vuelo.codigo_vuelo}, Origen: {vuelo.origen}, Estado: {vuelo.estado}, Terminal: {vuelo.terminal}, Puerta: {vuelo.puerta}")

def actualizar_vuelo():
    codigo_vuelo = input("Ingrese el código del vuelo a actualizar: ")
    for vuelo in vuelos:
        if vuelo.codigo_vuelo == codigo_vuelo:
            vuelo.aerolinea = input("Ingrese la nueva aerolínea: ")
            vuelo.hora_llegada = input("Ingrese la nueva hora de llegada: ")
            vuelo.origen = input("Ingrese el nuevo origen: ")
            vuelo.estado = input("Ingrese el nuevo estado: ")
            vuelo.terminal = input("Ingrese la nueva terminal: ")
            vuelo.puerta = input("Ingrese la nueva puerta: ")
            guardar_vuelos()
            print("¡Vuelo actualizado!")
            return
    print("Vuelo no encontrado.")

def borrar_vuelo():
    codigo_vuelo = input("Ingrese el código del vuelo a borrar: ")
    global vuelos
    vuelos = [vuelo for vuelo in vuelos if vuelo.codigo_vuelo != codigo_vuelo]
    guardar_vuelos()
    print("¡Vuelo borrado!")

def buscar_vuelo_por_campo(campo, valor):
    resultados = [vuelo for vuelo in vuelos if getattr(vuelo, campo) == valor]
    if resultados:
        for vuelo in resultados:
            print(f"Aerolínea: {vuelo.aerolinea}, Hora de llegada: {vuelo.hora_llegada}, Código de vuelo: {vuelo.codigo_vuelo}, Origen: {vuelo.origen}, Estado: {vuelo.estado}, Terminal: {vuelo.terminal}, Puerta: {vuelo.puerta}")
    else:
        print(f"No se encontraron vuelos para {campo} = {valor}.")

def menu():
    cargar_vuelos()
    while True:
        print("\nMenú de Vuelos")
        print("1. Crear vuelo")
        print("2. Leer vuelos")
        print("3. Actualizar vuelo")
        print("4. Borrar vuelo")
        print("5. Buscar vuelo por aerolínea")
        print("6. Buscar vuelo por hora de llegada")
        print("7. Buscar vuelo por código de vuelo")
        print("8. Buscar vuelo por origen")
        print("9. Buscar vuelo por estado")
        print("10. Buscar vuelo por terminal")
        print("11. Buscar vuelo por puerta")
        print("12. Salir")
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
            valor = input("Ingrese la aerolínea a buscar: ")
            buscar_vuelo_por_campo("aerolinea", valor)
        elif opcion == "6":
            valor = input("Ingrese la hora de llegada a buscar: ")
            buscar_vuelo_por_campo("hora_llegada", valor)
        elif opcion == "7":
            valor = input("Ingrese el código de vuelo a buscar: ")
            buscar_vuelo_por_campo("codigo_vuelo", valor)
        elif opcion == "8":
            valor = input("Ingrese el origen a buscar: ")
            buscar_vuelo_por_campo("origen", valor)
        elif opcion == "9":
            valor = input("Ingrese el estado a buscar: ")
            buscar_vuelo_por_campo("estado", valor)
        elif opcion == "10":
            valor = input("Ingrese la terminal a buscar: ")
            buscar_vuelo_por_campo("terminal", valor)
        elif opcion == "11":
            valor = input("Ingrese la puerta a buscar: ")
            buscar_vuelo_por_campo("puerta", valor)
        elif opcion == "12":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

menu()