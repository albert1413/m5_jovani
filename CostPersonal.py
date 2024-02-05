from classTreballador import Treballador

def calculaCostDelPersonal(treballadors: list):
    #Definim el preu de les hores pagades i el preu que li devem
    PreuHoresExtra = 20
    costFinal = 0
    for treballador in treballadors:
        if treballador.getTipusTreballador() in [Treballador.DIRECTOR,Treballador.SUBDIRECTOR]:
            #Si el treballador no es BASE no se li paguen les hores extra
            costFinal += treballador.getNomina()
        else:
            #Si el treballador es BASE se li paguen les hores extra
            costFinal += treballador.getNomina() + (treballador.getHoresExtres()*PreuHoresExtra)

    return costFinal
