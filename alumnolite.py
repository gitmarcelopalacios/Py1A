# importo la libreria de la base de datos
import sqlite3

# Conectar a la base de datos
def connect():
    conn = sqlite3.connect("jony.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacto (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        correo_electronico TEXT NOT NULL
    )
    """)
    conn.commit()
    return conn

# Cargar persona
def add_persona(conn, nombre, correo_electronico):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacto (nombre, correo_electronico) VALUES (?, ?)", (nombre, correo_electronico))
    conn.commit()

# Consultar personas
def get_contactos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacto")
    return cursor.fetchall()

# Actualizar persona
def update_persona(conn, id, nombre, direccion, telefono, correo_electronico):
    cursor = conn.cursor()
    cursor.execute("UPDATE persona SET nombre = ?, direccion = ?, telefono = ?, correo_electronico = ? WHERE id = ?", (nombre, direccion, telefono, correo_electronico, id))
    conn.commit()

# Eliminar persona
def delete_persona(conn, id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM persona WHERE id = ?", (id,))
    conn.commit()

# Buscar persona por ID
def get_persona_by_id(conn, id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM persona WHERE id = ?", (id,))
    return cursor.fetchone()

# Menú interactivo
def menu():
    conn = connect()
    while True:
        print("\nMenu:")
        print("1. Cargar Contacto")
        print("2. Actualizar Persona")
        print("3. Eliminar Persona")
        print("4. Consultar Contactos")
        print("5. Buscar Persona por ID")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            correo_electronico = input("Correo Electrónico: ")
            add_persona(conn, nombre, correo_electronico)
            print("Contacto agregada exitosamente!")
        elif opcion == '2':
            id = int(input("ID de la persona a actualizar: "))
            nombre = input("Nuevo nombre: ")
            direccion = input("Nueva dirección: ")
            telefono = input("Nuevo teléfono: ")
            correo_electronico = input("Nuevo correo electrónico: ")
            update_persona(conn, id, nombre, direccion, telefono, correo_electronico)
            print("Persona actualizada exitosamente!")
        elif opcion == '3':
            id = int(input("ID de la persona a eliminar: "))
            delete_persona(conn, id)
            print("Persona eliminada exitosamente!")
        elif opcion == '4':
            contactos = get_contactos(conn)
            for contacto in contactos:
                print(contacto)
        elif opcion == '5':
            id = int(input("ID de la persona a buscar: "))
            persona = get_persona_by_id(conn, id)
            if persona:
                print(persona)
            else:
                print("Persona no encontrada!")
        elif opcion == '6':
            print("¡Adiós!")
            break
        else:
            print("Opción no válida, intenta nuevamente.")

    conn.close()

# Ejecutar menú
if __name__ == "__main__":
    menu()
