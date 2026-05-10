import unittest
from calculadora import multiplicar

class TestCalculadora(unittest.TestCase):
    
    def test_multiplicar_positivos(self):
        self.assertEqual(multiplicar(3, 5), 15)
        
    def test_multiplicar_negativos(self):
        self.assertEqual(multiplicar(-2, 4), -8)
        self.assertEqual(multiplicar(-2, -3), 6)
        
    def test_multiplicar_por_cero(self):
        self.assertEqual(multiplicar(10, 0), 0)
        self.assertEqual(multiplicar(0, 5), 0)

    def test_multiplicar_decimales(self):
        self.assertAlmostEqual(multiplicar(2.5, 2), 5.0)

if __name__ == "__main__":
    unittest.main()
