#ejercicio excepciones m4s7 throw - mayor 18

def solicitar_edad():
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            return edad
        except ValueError:
            print("Error: Debes ingresar solo nros enteros. Inténtalo de nuevo.")

def verificar_adulto(edad):
    if edad >= 18:
        print("Eres adulto.")
    else:
        print("Eres menor de edad.")

# Programa principal
edad = solicitar_edad()
verificar_adulto(edad)
