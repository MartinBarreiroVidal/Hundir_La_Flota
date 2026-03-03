class Nave:
    # El "constructor": define los datos necesarios al instanciar
    def __init__(self, nombre, tamano):
        self.nombre = nombre       # Atributo: Nombre de la nave
        self.vida = tamano         # Atributo: Resistencia de la nave


    def recibir_disparo(self):
        self.vida -= 1
        return self.vida
