from tablero import Tablero

class Juego:
    def __init__(self):
        self.tablero = Tablero() # Creamos un tablero

    def mostrar_resultado(self, resultado):
        if resultado == 0: # Como pusimos en la clase tablero, agua es 0, entonces si el resultado coincide con 0, muestra "tocado"
            print("Agua")
        elif resultado == 1: # Si no es agua, como pusimos en la clase tablero, tocado es 1, entonces si el resultado coincide con 1, muestra "tocado"
            print("Tocado")
        elif resultado == 2: # Si no es agua ni tocado, como pusimos en la clase tablero, hundido es 2, entonces si el resultado coincide con 2, muestra "hundido"
            print("Hundido")
        elif resultado is None: # Si el resultado da None, muestra por pantalla "ya disparaste aquí"
            print("Ya disparaste aquí")

    def lanzar_ataque(self, x, y): # Lanzaremos el ataque en las coordenadas x e y
        print(f"\nAtaque en ({x},{y})") # Se muestra qué coordenadas estamos atacando

        resultado = self.tablero.comprobar_impacto(x, y) # Resultado de donde cae el ataque.

        self.mostrar_resultado(resultado) # Se muestra el resultado del ataque al usuario.

    def jugar_demo(self): # Aquí es donde determinamos las casillas donde queremos lanzar el ataque.
        self.lanzar_ataque(1, 1)
        self.lanzar_ataque(4, 3)
        self.lanzar_ataque(4, 3)
        self.lanzar_ataque(6, 6)


if __name__ == "__main__":
    juego = Juego()
    juego.jugar_demo()
