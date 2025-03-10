import os
import hashlib

DIRECTORIO_CLIENTES = "../clientes/"

# Tabla hash usando diccionario
tabla_clientes = {}

# Genera hash para nombre del cliente
def generar_hash(nombre):
    return hashlib.sha256(nombre.encode()).hexdigest()

# Crear archivo de cliente nuevo
def crear_cliente(nombre, servicio):
    cliente_hash = generar_hash(nombre)
    archivo_cliente = f"{DIRECTORIO_CLIENTES}{cliente_hash}.txt"
    if cliente_hash in tabla_clientes:
        print("Cliente ya existe. Intenta actualizar.")
        return False
    with open(archivo_cliente, 'w') as file:
        file.write(f"Cliente: {nombre}\n")
        file.write(f"Servicios:\n- {servicio}\n")
    tabla_clientes[cliente_hash] = archivo_cliente
    print(f"Cliente '{nombre}' creado exitosamente.")
    return True

# Actualizar cliente
def actualizar_cliente(nombre, nuevo_servicio):
    cliente_hash = generar_hash(nombre)
    archivo_cliente = tabla_clientes.get(cliente_hash)
    if archivo_cliente and os.path.exists(archivo_cliente):
        with open(archivo_cliente, 'a') as file:
            file.write(f"- {nuevo_servicio}\n")
        print(f"Servicio '{nuevo_servicio}' agregado al cliente '{nombre}'.")
        return True
    else:
        print("Cliente no encontrado.")
        return False

# Consultar cliente
def consultar_cliente(nombre):
    cliente_hash = generar_hash(nombre)
    archivo_cliente = tabla_clientes.get(cliente_hash)
    if archivo_cliente and os.path.exists(archivo_cliente):
        with open(archivo_cliente, 'r') as file:
            contenido = file.read()
        print(contenido)
        return contenido
    else:
        print("Cliente no encontrado.")
        return None

# Borrar cliente
def borrar_cliente(nombre):
    cliente_hash = generar_hash(nombre)
    archivo_cliente = tabla_clientes.get(cliente_hash)
    if archivo_cliente and os.path.exists(archivo_cliente):
        os.remove(archivo_cliente)
        del tabla_clientes[cliente_hash]
        print(f"Cliente '{nombre}' borrado correctamente.")
        return True
    else:
        print("Cliente no encontrado.")
        return False

# Listar clientes
def listar_clientes():
    if not tabla_clientes:
        print("No hay clientes registrados.")
    else:
        print("Clientes registrados:")
        for archivo in tabla_clientes.values():
            with open(archivo, 'r') as file:
                nombre_linea = file.readline()
                print(nombre_linea.strip())

# Menú interactivo
def menu():
    os.makedirs(DIRECTORIO_CLIENTES, exist_ok=True)
    while True:
        print("\n--- Menú Gestión Clientes ---")
        print("1. Crear nuevo cliente")
        print("2. Actualizar cliente existente")
        print("3. Consultar cliente")
        print("4. Borrar cliente")
        print("5. Listar clientes")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre del cliente: ")
            servicio = input("Descripción del servicio: ")
            crear_cliente(nombre, servicio)

        elif opcion == '2':
            nombre = input("Nombre del cliente existente: ")
            servicio = input("Nuevo servicio solicitado: ")
            actualizar_cliente(nombre, servicio)

        elif opcion == '3':
            nombre = input("Nombre del cliente a consultar: ")
            consultar_cliente(nombre)

        elif opcion == '4':
            nombre = input("Nombre del cliente a borrar: ")
            borrar_cliente(nombre)

        elif opcion == '5':
            listar_clientes()

        elif opcion == '6':
            break
        else:
            print("Opción no válida, intenta nuevamente.")

if __name__ == "__main__":
    menu()
