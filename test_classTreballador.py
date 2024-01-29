from classTreballador import Treballador
import unittest

class TreballadorTest(unittest.TestCase):

    def test_nom_treballador_incorrecte(self):
        treballador_meu = Treballador()
        excepcio_meva = self.assertRaises(Exception, lambda: 
            treballador_meu.set_nom(""))
        self.assertEqual("El nom ha de tenir 3 o més caràcters", excepcio_meva.message)
        
    def test_nom_treballador_correcte(self):
    
        nom_test = "Montsià"
        treballador = Treballador()
        try:
            treballador.set_nom(nom_test)
        except Exception as e:
            print(e.message)
        self.assertEqual(nom_test, treballador.get_nom(), "Els noms han de coincidir!!!")

    def test_nomina(self):
        nomina = 2300
        treballador = Treballador()
        treballador.set_nomina(nomina)
        self.assertEqual(nomina, treballador.get_nomina(), "Els dos valors de la nomina han de coincidir!!!")

    def test_hores_extres(self):
        hores_extres = 10
        treballador = Treballador()
        treballador.set_hores_extres(hores_extres)
        self.assertEqual(hores_extres, treballador.get_hores_extres(), "Els dos valors de les hores extres han de coincidir!!!")

    def test_tipus_treballador_incorrecte(self):
        treballador = Treballador()
        with self.assertRaises(Exception) as context:
            treballador.set_tipus_treballador("DIREKTOR")
        self.assertEqual("Tipus de treballador no vàlid", str(context.exception))

    def test_tipus_treballador_correcte(self):
        treballador_meu = Treballador("pepa",1,2500,10)
        with self.assertRaises(Exception) as cm:
            treballador_meu.set_tipus_treballador("DIRECTOR")
            self.assertEqual(str(cm.exception), 'Tipus de treballador no vàlid')

if __name__ == '__main__':
    unittest.main()