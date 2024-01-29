from CostPersonal import calculaCostDelPersonal
from classTreballador import Treballador
import unittest

def test_calculaCostDelPersonal(treballadors: list):
    costFinal = 0
    for treballador in treballadors:
        if treballador.getTipusTreballador() in [Treballador.DIRECTOR,Treballador.SUBDIRECTOR]:
            costFinal += treballador.getNomina()
        else:
            costFinal += treballador.getNomina() + (treballador.getHoresExtres()*20)

    return costFinal
