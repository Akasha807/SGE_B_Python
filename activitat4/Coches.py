class Coches:
    # Constructor
    def __init__(self, marca, modelo, color, motor, puertas):
        # Atributos
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.puertas = puertas

    # Getters y Setters
    def get_marca(self):
        return self.marca

    def set_marca(self, new_marca):
        self.marca = new_marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, new_modelo):
        self.modelo = new_modelo

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def get_motor(self):
        return self.motor

    def set_motor(self, new_motor):
        self.motor = new_motor

    def get_puertas(self):
        return self.puertas

    def set_puertas(self, new_puertas):
        self.puertas = new_puertas

