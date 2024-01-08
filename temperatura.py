def main():
    '''Identificar variables'''
    a = int(input("Escriu la temperatura en Graus Celsius:"))

    '''Calent'''
    if a>30:
        if a>=100:
            print("Estàs hot. L'aigua està bullint.")
        else:
            print("Estàs hot")
    '''Fred'''
    if a<10:
        if a<=0:
            print("Pecho frio. L'aigua és congelarà.")
        else:
            print("Pecho frio")
    '''Normal'''
    if 10<=a<=30:
        print("Estàs god")

main()
