class Producte:
    SENSE_IVA = 0
    AMB_IVA = 1
    
    IVA = 1.05
    
    def total_factura(llista):
        total = 0
        for item in llista:
            total += Producte.cost_tax(item) if item.tipus == Producte.AMB_IVA else item.costBase
        return total

    def cost_tax(producte):
        return producte.costBase * Producte.IVA

    def producte_amb_iva(cls, nom, costBase):
        return cls(nom, cls.AMB_IVA, costBase)

    def producte_sense_iva(cls, nom, costBase):
        return cls(nom, cls.SENSE_IVA, costBase)