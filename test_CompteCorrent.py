from CompteCorrent import CompteCorrent
import unittest

class TestCompteCorrent(unittest.TestCase):

    def test_dipositar(self):
        compte = CompteCorrent(100, "123456")
        compte.dipositar(50)
        self.assertEqual(compte.saldo, 150)

    def test_retirar_contrasenya_incorrecta(self):
        compte = CompteCorrent(100, "123456")
        with self.assertRaises(Exception) as context:
            compte.retirar(50, "654321")
        self.assertEqual(str(context.exception), "Contrasenya incorrecta")

    def test_retirar_saldo_insuficient(self):
        compte = CompteCorrent(100, "123456")
        with self.assertRaises(Exception) as context:
            compte.retirar(150, "123456")
        self.assertEqual(str(context.exception), "Saldo insuficient")

    def test_retirar_exitosament(self):
        compte = CompteCorrent(100, "123456")
        self.assertEqual(compte.retirar(50, "123456"), 50)

    def test_getSaldo_contrasenya_incorrecta(self):
        compte = CompteCorrent(100, "123456")
        with self.assertRaises(Exception) as context:
            compte.getSaldo("654321")
        self.assertEqual(str(context.exception), "Contrasenya incorrecta")

    def test_getSaldo_exitosament(self):
        compte = CompteCorrent(100, "123456")
        self.assertEqual(compte.getSaldo("123456"), 100)

    def test_setContrasenya_contrasenya_incorrecta(self):
        compte = CompteCorrent(100, "123456")
        with self.assertRaises(Exception) as context:
            compte.setContrasenya("654321", "new_pass")
        self.assertEqual(str(context.exception), "Contrasenya incorrecta")

    def test_setContrasenya_exitosament(self):
        compte = CompteCorrent(100, "123456")
        self.assertEqual(compte.setContrasenya("123456", "new_pass"), 0)

if __name__ == '__main__':
    unittest.main()
