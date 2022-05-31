n = float(input("Digite o número que você quer saber a raiz quadrada: "))
i = 1
controle = 1
while controle <= n :
    i *= i 
    i+=1
    controle +=1
print(i)