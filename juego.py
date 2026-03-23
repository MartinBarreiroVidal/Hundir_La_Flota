from nave import Nave
from tablero import Tablero
class Juego:
    def __init__(self):
        """
        Constructor de la clase juego.
        Inicializamos el tablero y las naves del juego
        """

        self.lanzar_ataque(1,1)

    def inicializar_naves(self):
        """
        Crea e inicializa todas las naves del juego
        Coloca las naves en el tablero en posiciones predefinidas
        :return:
        """

    def mostrar_resultado(self, resultado:int):
        """
        Muestra el resultado del disparo
        Args:
            resultado (str)
        """
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")


    def lanzar_ataque(self, x, y):
        """
        Ejecuta un disparo en las coordenadas indicadas
        Si impacta una nave y su vida llega a cero,
        :args
        x(int): coordenada x del disparo
        y(int): coordenada y del tablero

        """
        print(f"Atacando a {x}, {y}")
        obj_tablero = Tablero()
        resultado = obj_tablero.comprobar_impacto(x,y)
        self.mostrar_resultado(resultado)

if __name__ == "__main__":
    Juego()