num1 = int(input("Digite um numero: "))

if(num1 > 10):
    print("O valor e maior que 10!")
    if(num1<=15):
        print("O valor e maior que 10, e menor que 15")
    else:
        if(num1<=50):
            print("O valor e maior do que 10, e menor que 50")
        else:
            print("O valor e maior que 50")
else:
    if(num1>5):
        print("O numero e menor do que 10 mas maior que 5!")
        if(num1==7):
            print("O numero e igual a 7!")
        else:
            print("O valor e maior que 5!")