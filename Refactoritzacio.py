class Producte:
    SENSE_IVA = 0
    AMB_IVA = 1
    
    IVA = 1.05
    
    def costProducte(producte: Producte):
        preu = 0
        if(producte.tipus == Producte.AMB_IVA):
            preu += producte.costBase*Producte.IVA
        else:
            preu += producte.costBase
        return preu
    
    def totalFactura(llista: list):
        total = 0
        for item in llista:
            total += costProducte(item)
        return total

    
