import unittest
def suma(a,b):
    return a + b
class cajanegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        a = 10
        b = 5

        resultado = suma(a,b)

        self.assertEqual(resultado, 15)
    def test_suma_dos_negativos(self):
        a = -10
        b = -7

        resultado = suma(a,b)
        self.assertEqual(resultado, -17)


if __name__ == '__main__':
    unittest.main()