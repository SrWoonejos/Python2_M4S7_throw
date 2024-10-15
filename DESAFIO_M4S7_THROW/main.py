#desafio m4s7 excepciones throw
#clase excepcion 
class RangoSalarioError(Exception):
    def __init__(self, salario, mensaje = "El salario debe estar entre los $1000 y $2000") -> None:
        self.salario = salario
        self.mensaje = mensaje
        super().__init__(f"{salario} -> {mensaje}")

#excepcion personalizada que muestra salario fuera de rango
def verificar_salario(salario):
    if salario < 1000 or salario > 2000:
        #msj excepcion
        raise RangoSalarioError(salario)
    else:
        print("Salario aceptado")
        return True

#programa principal usuario
while True:
    try:
        salario = int(input("Ingresa tu salario: "))
        if verificar_salario(salario):
            break #se rompe buble cuando el salario esta dentro del rango
    except RangoSalarioError as e:
        print(e)
    except ValueError:
        print("Error: Ingresa nros enteros")  