class Nave:
    # El "constructor": define los datos necesarios al instanciar
    def __init__(self, nombre, tamano, tipo):
        """
        Constructor de la clase Nave.

        Args:
            nombre (str): Nombre del barco (Submarino, Buque, Portaaviones)
            tamano (int): Tamaño de la nave (número de casillas que ocupa)
        """
        self.nombre = nombre       # Atributo: Nombre de la nave
        self.vida = tamano         # Atributo: Resistencia de la nave
        self.tipo = tipo


    def recibir_disparo(self):
        """
            Procesa el impacto de un disparo en la nave.
            Reduce la vida de la nave y devuelve el estado (Tocado/Hundido).

            Returns:
            str: Estado de la nave tras el disparo ("Tocado", "Hundido", etc.)
        """
        self.vida = self.vida -1
        return

