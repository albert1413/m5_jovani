def main():
    a = int(input("Escriu la temperatura en Graus Celsius:"))

    if a>30:
        if a>=100:
            print("Estàs hot. L'aigua està bullint.")
        else:
            print("Estàs hot")

    if a<10:
        if a<=0:
            print("Pecho frio. L'aigua és congelarà.")
        else:
            print("Pecho frio")

    if 10<=a<=30:
        print("Estàs god")

main()
