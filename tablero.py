from nave import Nave
class Tablero:
    def __init__(self):
        self.agua = 0
        self.tocado = 1
        self.hundido = 2

    def colocar_nave (self, nave,x,y,orientacion):
        """
        Coloca una nave en el tablero en las coordenadas especificadas.
        Marca las casillas ocupadas por la nave según su tamaño y orientación.

        Args:
            nave (Nave): Objeto nave a colocar
            x (int): Coordenada X inicial (fila)
            y (int): Coordenada Y inicial (columna)
            orientacion (str): Orientación de la nave
                              "H" para horizontal (expande en columnas)
                              "V" para vertical (expande en filas)

        Example:
            tablero.colocar_nave(submarino, 0, 0, "H")  # Coloca horizontalmente desde (0,0)
            tablero.colocar_nave(buque, 5, 3, "V")      # Coloca verticalmente desde (5,3)
        """
        pass

    def comprobar_impacto(self, x, y):
        self.submarino1 = nave
        print("(LOG) Estoy en tablero comprobando el impacto")
        return self.agua


