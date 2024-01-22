class Treballador:
'''Coloquem una classe per a l'informació dels treballadors'''

    def __init__(self, nom="", tipus=BASE, nomina=0.0, hores=0):
        '''En aquesta funció es podra almacenar el nom, el tipus, la nomina i les hores'''
        self.nomTreballador = nom
        self.tipusTreballador = tipus
        self.nominaTreballador = nomina
        self.horesExtresTreballador = hores

    def set_nom(self, nom):
        '''Aquesta funció es per a comprovar que siguin noms de més de 2 caracters'''
        if len(nom) < 3:
            raise Exception("El nom ha de tenir 3 o més caracters")
        self.nomTreballador = nom

    def get_nom(self):
        '''Aquesta funció ensenya el nom que te el treballador'''
        return self.nomTreballador

    def set_nomina(self, euros):
        '''Aquesta funció serveix per definir la nomina del treballador'''
        self.nominaTreballador = euros

    def get_nomina(self):
        '''Aquesta funció ensenya la nomina que te el treballador'''
        return self.nominaTreballador

    def set_hores_extres(self, hores):
        '''Aquesta funció serveix per definir les hores que treballar el treballador'''
        self.horesExtresTreballador = hores

    def get_hores_extres(self):
        '''Aquesta funció ensenya les hores que fa el treballador'''
        return self.horesExtresTreballador

    def set_tipus_treballador(self, tipus):
        '''Aquesta funció serveix per definir el carreg que ocupa'''
        if tipus in [self.DIRECTOR, self.SUBDIRECTOR, self.BASE]:
            self.tipusTreballador = tipus
        else:
            raise Exception("Tipus de treballador no vàlid")

    def get_tipus_treballador(self):
        '''Aquesta funció ensenya el carreg que ocupa el treballador'''
        return self.tipusTreballador