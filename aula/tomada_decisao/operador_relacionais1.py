"""Operadores relacionais
(>) MAIOR QUE
(<) MENOR QUE
(>=) MAIOR OU IGUAL QUE
(<=) MENOR IGUAL QUE"""

idade = int(input("Digite sua idade: "))
if(idade<=0):
    print("SUA IDADE NAO PODE SER 0 OU MENOR QUE 0 !")
else:
    if(idade>150):
        print("A SUA IDADE NAO PODE SER MAIOR QUE 150 ANOS !")
    else:
        if(idade<18):
            print("VOCE PRECISA TER MAIS DE 18 ANOS !")