ip = float(input("Digite o IP: "))

if((ip >= 0) & (ip <= 127)):
    print("Classe A !")
else:
    if ((ip >= 128) & (ip <= 191)):
        print("Classe B !")
    else:
        if ((ip >= 192) & (ip <= 223)):
            print("Classe C !")
        else:
            if ((ip >= 224) & (ip <= 239)):
                print("Classe A !")
            else:
                if ((ip >= 240) & (ip <= 999)):
                    print("Classe A !")
                else:
                    print("INFOME UMA SINTAX CORRETA !")