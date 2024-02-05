import unittest
from CompteCorrent import CompteCorrent

class TestCompteCorrent(unittest.TestCase):
    def test_dipositar(self):
        compte = CompteCorrent(100, "123456")
        compte.dipositar(50)
        self.assertEqual(compte.saldo, 150)

    def test_retirar_contrasenya_incorrecta(self):
        compte = CompteCorrent(100, "123456")
        self.assertEqual(compte.retirar(50, "654321"), -2)

    def test_retirar_saldo_insuficient(self):
        compte = CompteCorrent(100, "123456")
        self.assertEqual(compte.retirar(150, "123456"), -1)

    def test_retirar_exitosament(self):
        compte = CompteCorrent(100, "123456")
        self.assertEqual(compte.retirar(50, "123456"), 50)

    def test_getSaldo_contrasenya_incorrecta(self):
        compte = CompteCorrent(100, "123456")
        self.assertEqual(compte.getSaldo("654321"), -2)

    def test_getSaldo_exitosament(self):
        compte = CompteCorrent(100, "123456")
        self.assertEqual(compte.getSaldo("123456"), 100)

    def test_setContrasenya_contrasenya_incorrecta(self):
        compte = CompteCorrent(100, "123456")
        self.assertEqual(compte.setContrasenya("654321", "new_pass"), -2)

    def test_setContrasenya_exitosament(self):
        compte = CompteCorrent(100, "123456")
        self.assertEqual(compte.setContrasenya("123456", "new_pass"), 0)

if __name__ == '__main__':
    unittest.main()