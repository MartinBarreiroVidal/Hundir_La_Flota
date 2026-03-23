from tablero import Tablero

class Juego:
    def __init__(self):
        """
        Constructor de la clase Juego.
        Creamos UN SOLO tablero para toda la partida.
        """
        self.tablero = Tablero()

        self.lanzar_ataque(1, 1)   # Primer disparo -> Tocado

    def mostrar_resultado(self, resultado: int):
        """
        Muestra el resultado del disparo.

        Args:
            resultado (int)
        """
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")
        elif resultado == 3:
            print("Casilla ya disparada")

    def lanzar_ataque(self, x, y):
        """
        Ejecuta un disparo en las coordenadas indicadas.
        """
        print(f"\nAtacando a {x}, {y}")
        resultado = self.tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)

if __name__ == "__main__":
    Juego()