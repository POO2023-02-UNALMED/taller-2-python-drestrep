class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor 
        self.registro = registro

    def cantidadAsientos(self):
        c = 0
        for i in self.asientos:
            if i != None:
                c += 1
        return c
        
        
    def verificarIntegridad(self):
        for i in self.asientos:
            if self.registro != i.registro:
                return "Las piezas no son originales"
            
            if self.registro != self.motor.registro:
                return "Las piezas no son originales"
            else:
                return "Auto original"




class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

class Asiento:
    colores = ["rojo", "verde", "amarillo", "negro","blanco"]
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in Asiento.colores:
            self.color = color

