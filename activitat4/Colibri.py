class Colibri:
    # Constructor
    def __init__(self, nombre, tamaño, edad, velocidad_ala, region):
        self.nombre = nombre
        self.tamaño = tamaño
        self.edad = edad
        self.velocidad_ala = velocidad_ala
        self.region = region

    # Métodos Getters y Setters

    # Nombre
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    # Tamaño
    def get_tamaño(self):
        return self.tamaño

    def set_tamaño(self, nuevo_tamaño):
        self.tamaño = nuevo_tamaño

    # Edad
    def get_edad(self):
        return self.edad

    def set_edad(self, nueva_edad):
        self.edad = nueva_edad

    # Velocidad de las alas
    def get_velocidad_ala(self):
        return self.velocidad_ala

    def set_velocidad_ala(self, nueva_velocidad):
        self.velocidad_ala = nueva_velocidad

    # Región
    def get_region(self):
        return self.region

    def set_region(self, nueva_region):
        self.region = nueva_region
