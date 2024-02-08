from classTreballador import Treballador

class CostPersonal:
    def calculaCostDelPersonal(treballadors):
        #Definim el preu de les hores pagades i el preu que li devem
        PreuHoresExtra = 20
        costFinal = 0
        if Treballador.get_tipus_treballador in [Treballador.DIRECTOR,Treballador.SUBDIRECTOR]:
            #Si el treballador no es BASE no se li paguen les hores extra
            costFinal += Treballador.get_nomina
        else:
            #Si el treballador es BASE se li paguen les hores extra
            costFinal += Treballador.get_nomina + (Treballador.get_hores_extres*PreuHoresExtra)

        return costFinal
