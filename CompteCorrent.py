class CompteCorrent:
    pasta = 0

    def __init__(self, saldoIncial, cs):
        self.saldo = saldoIncial
        self.contrasenya = cs

    def dipositar(self, pasta:float) -> float:
        pasta += self.saldo
        
    
    def retirar(self, pasta: float, cs: str) -> float:
        y = float(input("Diners que vols retirar:"))
        x = input("Contrasenya:")
        if x == cs and y <=pasta:
            return True
        if x != cs:
            return -2
        elif y > pasta:
            return -1
    
    def getSaldo(self, cs: str) -> float:
        if self.retirar.x == cs:
            return self.depositar.pasta
        else:
            return -2
    
    def setContrasenya(self, antiga: str, nova: str) -> int:
        ''' Modifica la contrasenya, torna 0 si va bé i -2 si l'antiga és incorrecta '''
        antiga = self.contrasenya
        if self.retirar.x == antiga:
            nova = input("Canvia la contrasenya:")
            antiga = nova
            return 0
        else:
            return -2