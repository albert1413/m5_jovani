import unittest

from checknumber import comprova_signe

class TestSum(unittest.TestCase):
    
    def positiu(self):
        '''Comprovació del signe positiu'''
        resultat = comprova_signe(1)
        self.assertEqual(resultat, 1)

    
    def nul(self):
        '''Comprovació de 0'''
        resultat = comprova_signe(0)
        self.assertEqual(resultat, 0)

    
    def negatiu(self):
        '''Comprovació del signe negatiu'''
        resultat = comprova_signe(-3)
        self.assertEqual(resultat, -1)


if __name__ == "__main__":
    unittest.main()