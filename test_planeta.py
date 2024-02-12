from planeta import Planeta
import unittest

class PlanetaTest(unittest.TestCase):
    
    def testConversioKelvin(self):
        planeta = Planeta(25, 40, 20, 9.8, 150)
        self.assertEquals(planeta.de_celsius_a_kelvin(), 298)

    def testPlanetaHabitable(self):
        planeta1 = Planeta(25, 40, 20, 9.8, 150)
        planeta2 = Planeta(16, 40, 20, 9.8, 150)
        planeta3 = Planeta(45, 20, 24, 9.8, 180)
        planeta4 = Planeta(25, 40, 26, 9.8, 160)

        self.assertEquals(planeta1.es_habitable(), 1)
        self.assertEquals(planeta2.es_habitable(), 0)
        self.assertEquals(planeta3.es_habitable(), 0)        
        self.assertEquals(planeta4.es_habitable(), 0)

    def testCalculPes(self):
        # assertEquals(expected, actual)
        pass

    def testPlanetaEquilibrat(self):
        # assertEquals(expected, actual)
        # assertEquals(expected, actual)
        pass

if __name__ == '__main__':
    unittest.main()s