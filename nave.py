class Nave:
    TOCADO = 1 # TOCADO será 1
    HUNDIDO = 2 # HUNDIDO será 2

    def __init__(self, nombre, tipo, vida): # Aquí inicializamos la nave dandole valores
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.hundido = False

    def recibir_disparo(self):
        if self.hundido:
            return self.HUNDIDO

        self.vida -= 1

        if self.vida <= 0: # Si la vida es menor o igual que 0, la nave está hundida (self.hundido = True)
            self.vida = 0
            self.hundido = True
            print(f"{self.nombre} hundido") # Saca por pantalla el nombre de la nave y que está hundida.
            return self.HUNDIDO # Retorna resultado TOCADO ya el barco ha sido golpeado y no tiene vida (self.vida=0).
        else:
            print(f"{self.nombre} tocado. Vida restante: {self.vida}") # Muestra el nombre de la nave, que está tocada y la vida que le falta.
            return self.TOCADO # Retorna resultado TOCADO ya el barco ha sido golpeado pero sigue con vida.