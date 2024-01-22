/class Treballador:
    """Classe per a guardar les dades d'un treballador"""
    DIRECTOR = 0
    SUBDIRECTOR = 1
    BASE = 2

    def __init__(self, nom, tipus, nomina, hores):
        #Constructor amb arguments, alternatiu al constructor per defecte
        self.nomTreballador = nom
        self.tipusTreballador = tipus
        self.nominaTreballador = nomina
        self.horesExtresTreballador = hores

    def setNom(self, nom):
        #Si la longitud del nou nom es inferior a tres caracters llença
excepcio
        if len(nom) < 3:
            raise Exception("El nom ha de tenir 3 o més caracters")
        #En cas contrari assigna el nom
        self.nomTreballador = nom
    
    def getNom(self):