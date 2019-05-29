num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
num3 = int(input("Digite mais um valor: "))

if((num1 > num2) & (num1 > num3)):
        print("Numero 1 maior: ", num1)
else:
    if((num2 > num1) & (num2 > num3)):
            print("Numero 2 maior: ", num2)
    else:
        if((num3 > num2) & (num3 > num2)):
            print("Numero 3 maior: ", num3)