from unittest import TestCase
   

class TestCarro(TestCase):
    def test_mover(self):
        mi_carro = Carro('SYJ-123', 'Rosa')
        print(f'--- inicia la prueba de conduccion para el carro {mi_carro}')
        #Probar que no se mueve si no que està encendido
        espero = Exception('El carro no esta encendido')
        print(type(espero))


    def test_reserva(self):
        self.fail()

    def test_encender(self):
        self.fail()

    def test_frenar(self):
        self.fail()º
