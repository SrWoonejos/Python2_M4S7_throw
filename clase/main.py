#

class Cliente:
    def __init__(self, id, nombre, saldo):
        self.id = id
        self.nombre = nombre
        self.saldo = saldo

    def get_saldo(self):
        return self.saldo


# Definición de una excepción personalizada
class MyError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return repr(self.mensaje)


def comprar(cliente, precio):
    """Función que intenta realizar la compra para un cliente"""
    try:
        if cliente.get_saldo() < precio:
            raise MyError(f"Compra rechazada. Cliente {cliente.id} - {cliente.nombre}, tu saldo de {cliente.saldo} no es suficiente para una compra de {precio}.")
        else:
            cliente.saldo -= precio
            print(f"Gracias por tu compra, Cliente {cliente.id} - {cliente.nombre}. Tu saldo restante es {cliente.saldo}.")
    except MyError as error:
        print(f"Error: {error}")


# Función para crear un cliente de manera segura
def crear_cliente():
    while True:
        try:
            id_cliente = int(input("Ingrese el ID del cliente (número entero): "))
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            saldo_cliente = float(input("Ingrese el saldo del cliente (número decimal o entero): "))
            return Cliente(id_cliente, nombre_cliente, saldo_cliente)
        except ValueError:
            print("Entrada inválida. El ID debe ser un número entero y el saldo un número válido.")


# Función para solicitar el precio de manera segura
def solicitar_precio():
    while True:
        try:
            return float(input("Ingrese el precio del producto (número decimal o entero): "))
        except ValueError:
            print("Entrada inválida. El precio debe ser un número válido.")


def menu_principal():
    print("\n=== Bienvenido a la tienda ===")
    print("1. Realizar una compra")
    print("2. Salir")
    while True:
        try:
            opcion = int(input("Seleccione una opción (1 o 2): "))
            if opcion in [1, 2]:
                return opcion
            else:
                print("Opción inválida. Seleccione 1 para comprar o 2 para salir.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero (1 o 2).")


# Bucle principal del programa
while True:
    opcion = menu_principal()

    if opcion == 1:
        # Crear dos clientes interactivos
        print("\n=== Cliente 1 ===")
        cliente1 = crear_cliente()

        print("\n=== Cliente 2 ===")
        cliente2 = crear_cliente()

        # Solicitar precios para los productos
        print("\n=== Precio de productos ===")
        precio1 = solicitar_precio()
        precio2 = solicitar_precio()

        # Realizar compras
        comprar(cliente1, precio1)  # Intentar comprar con el primer cliente
        comprar(cliente2, precio2)  # Intentar comprar con el segundo cliente
    elif opcion == 2:
        print("Gracias por usar nuestro sistema. ¡Hasta pronto!")
        break  # Terminar el programa
