def comprova_signe(num: int)->int:
    
    resultat = 0
    
    if(num>0):
        resultat = 1
    elif(num==0):
        resultat = 0
    else:
        resultat = -1
        
    return resultat
