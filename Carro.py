from Vehiculo import Vehiculo

class Carro(Vehiculo):

    def __init__(self, n_ruedas, placa, color):
        super().__init__(4, placa, color)

    def mover(self):
        super().mover()

    def reserva(self):
        super().reserva()

    def encender(self):
        return super().encender()

    def frenar(self):
        super().frenar()