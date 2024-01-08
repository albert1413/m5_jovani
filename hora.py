def main():
    '''Identificar variables'''
    a =float(input("Escriu un número de segons:"))
    b =float(input("Escriu un número de minuts:"))
    c =float(input("Escriu un número de hores:"))

    '''Calcula el total de segons'''
    n = (a + b*60 + c*3600)

    '''Calcul de els dies, les hores, els minuts i els segons'''
    d = n // 86400
    z = n % 86400 // 3600
    m = n % 86400 % 3600 // 60
    s = n % 86400 % 3600 % 60

    print("d=",d,":h=", z,":m=", m,":s=", s,)
main() 