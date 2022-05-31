num = int(input("Digite um número para saber quantos divisores tem: "))

i = 1
soma = 0
while i <= num:
    if num % i == 0:
        soma+=1
    i+=1
print("O numero escolhido tem {} divisores.".format(soma))
    