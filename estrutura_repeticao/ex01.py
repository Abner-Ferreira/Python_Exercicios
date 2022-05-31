num = int(input("Digite um número inteiro: "))
soma = 0

while num != 0 :
    resto = num%2

    if resto == 0:
        soma += resto
    num = int(input("Digite um número inteiro: "))
print(soma)  
