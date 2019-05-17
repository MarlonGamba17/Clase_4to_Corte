from unittest import TestCase
from Vehiculo import Vehiculo


class TestVehiculo(TestCase):

    def test_encender(self):

        # valido la inicializacion del vehiculo
        print('---Inicia prueba de creación del vehiculio ---')
        dado = Vehiculo(4, 'BAD-768', 'Plata')
        espero = False
        recibo = dado.encendido
        self.assertEqual(espero, recibo)

        # valido la inicializacion del vehiculo
        print('---Inicia prueba de encendido del vehiculio ---')
        espero = True
        recibo = dado.encender()
        self.assertEqual(espero, recibo)

        #valido la inicializacion del vehiculo
        print('---Inicia prueba de apagado del vehiculio ---')
        espero = False
        recibo = dado.encender()
        self.assertEqual(espero, recibo)