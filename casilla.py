class Casilla:
    def __init__(self):
        self.nave = None # No hay naves en esta casilla
        self.visitada = False # Esta casilla ya fue visitada/disparada

    def disparar(self): # Aquí determinamos el estado de la casilla
        if self.visitada: # Si ocurre esto, muestra por pantalla que aquí ya se disparó.
            print("Ya disparaste aquí")
            return None

        self.visitada = True

        if self.nave is None: # Si la naves es None significa que no hay naves en esa casilla, entonces muestra "Agua".
            print("Agua")
            return 0

        return self.nave.recibir_disparo()