# Archivo principal para instanciar objetos de las clases Coches y Colibri
from Coches import Coches
from Colibri import Colibri

# Instancia objetos Coches 
coche1 = Coches("Tesla", "Model S", "Rojo", "Eléctrico", 4)
coche2 = Coches("Ferrari", "LaFerrari", "Amarillo", "Híbrido", 2)
coche3 = Coches("Bugatti", "Chiron", "Azul", "Gasolina", 2)

# Instancia objetos Colibri
colibri1 = Colibri("Colibrí Verde Esmeralda", "Pequeño", 3, 80, "Bosques tropicales")
colibri2 = Colibri("Colibrí Rosado", "Muy pequeño", 2, 100, "Selvas")
colibri3 = Colibri("Colibrí Azul", "Pequeño", 4, 120, "Montañas")

# Mostrar tres getters de Coches
print("Marca del primer coche:", coche1.get_marca())
print("Modelo del segundo coche:", coche2.get_modelo())
print("Color del tercer coche:", coche3.get_color())

# Mostrar cuatro getters de Colibri
print("Especie del primer colibrí:", colibri1.get_nombre())
print("Tamaño del segundo colibrí:", colibri2.get_tamaño())
print("Edad del tercer colibrí:", colibri3.get_edad())
print("Velocidad de vuelo del primer colibrí:", colibri1.get_velocidad_ala())

# Modificar dos atributos de Coches a través de los setters
coche1.set_modelo("Model X")
coche2.set_motor("Híbrido Avanzado")

# Mostrar los atributos modificados de Coches a través de los getters
print("Nuevo modelo del primer coche:", coche1.get_modelo())
print("Nuevo tipo de motor del segundo coche:", coche2.get_motor())

# Modificar dos atributos de Colibri a través de los setters
colibri1.set_nombre("Colibrí Cora")
colibri2.set_tamaño("Mediano")

# Mostrar los atributos modificados de Colibri a través de los getters
print("Nuevo nombre del primer colibrí:", colibri1.get_nombre())
print("Nuevo tamaño del segundo colibrí:", colibri2.get_tamaño())
