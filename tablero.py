from nave import Nave
class Tablero:
    def __init__(self):
        self.agua = 0
        self.tocado = 1
        self.hundido = 2

    def comprobar_impacto(self, x, y):

        print("(LOG) Estoy en tablero comprobando el impacto")
        return self.agua

