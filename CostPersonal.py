from classTreballador import Treballador

def calculaCostDelPersonal(treballadors: list):
    PreuHoresExtra = 20
    costFinal = 0
    for treballador in treballadors:
        if treballador.getTipusTreballador() in [Treballador.DIRECTOR,Treballador.SUBDIRECTOR]:
            costFinal += treballador.getNomina()
        else:
            costFinal += treballador.getNomina() + (treballador.getHoresExtres()*PreuHoresExtra)

    return costFinal
