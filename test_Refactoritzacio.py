from Refactoritzacio import Producte
import unittest

class TestProducte(unittest.TestCase):
    def test_total_factura(self):
        llista_productes = [
            Producte("Producte1", Producte.AMB_IVA, 100),
            Producte("Producte2", Producte.SENSE_IVA, 200)
        ]
        self.assertEqual(Producte.total_factura(llista_productes), 100 * 1.05 + 200)

    def test_cost_tax(self):
        producte_amb_iva = Producte("Producte1", Producte.AMB_IVA, 100)
        self.assertEqual(Producte.cost_tax(producte_amb_iva), 100 * 1.05)

    def test_producte_amb_iva(self):
        producte_amb_iva = Producte.producte_amb_iva("Producte1", 100)
        self.assertEqual(producte_amb_iva.tipus, Producte.AMB_IVA)

    def test_producte_sense_iva(self):
        producte_sense_iva = Producte.producte_sense_iva("Producte2", 200)
        self.assertEqual(producte_sense_iva.tipus, Producte.SENSE_IVA)

if __name__ == '__main__':
    unittest.main()