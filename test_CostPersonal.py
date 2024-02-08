from CostPersonal import CostPersonal
from classTreballador import Treballador
import unittest

class Test_CostPersonal(unittest.TestCase):
    def test_calculaCostnohores(self):
        treballadors = [Treballador("John", Treballador.DIRECTOR, 3000, 0)]
        x = CostPersonal.calculaCostDelPersonal(treballadors)
        self.assertEqual(x, CostPersonal.calculaCostDelPersonal(treballadors))

if __name__ == '__main__':
    unittest.main()
