class Planeta:
  """
  DOCUMENTAR
  """
  def __init__(self, temperaturaMitjana, quantitatAigua, radiacio, gravetat, distanciaSol):
    """
    Definim els parametres del planeta(temperaturaMitjana, quantitatAigua...)
    """
    self.temperaturaMitjana = temperaturaMitjana
    self.quantitatAigua = quantitatAigua
    self.radiacio = radiacio
    self.gravetat = gravetat
    self.distanciaSol = distanciaSol
  
  def set_distancia_al_sol(self, distanciaSol):
    """
    Utilitzem aquesta funció per definir que la distancia no pot ser negativa
    """
    if (self.distanciaSol < 0):
      raise Exception("La distància no pot ser negativa")
    self.distanciaSol = distanciaSol

  def de_celsius_a_kelvin(self):
    """
    Aquesta funció ajuda a calcular la temperatura en graus Kelvins
    """
    return self.temperaturaMitjana + 273
    
  def es_habitable(self):
    """
    Aquesta funció tornarà un 1 si es compleixen tres condicions i per tant, voldra dir que es habitable
    """
    if 20 <= self.temperaturaMitjana <= 45 and self.quantitatAigua == 40 and self.radiacio < 25:
      return 1
    else:
      return 0
      

  def pes_persona_en_newtons(self, pesPersona):
    """
    Aquesta funció calculara el pes de la persona en un planeta en newtons 
    """
    return pesPersona * self.gravetat
  
  def planeta_equilibrat(self):
    """
    Aquesta funció comprovara que el planeta estigui equilibrat o no 
    Per fer-ho, comprovara que la quantitat d'aigua sigui igual a 
    la divisió entre distanciaSol i radiacio. 1=equilibrat i 2=No_equilibrat
    """
    y = self.distanciaSol/self.radiacio
    if y == self.quantitatAigua:
      return 1
    else:
      return 0

