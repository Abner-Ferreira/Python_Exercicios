import random
sorteado = random.randint(1,1001)
chute = int(input("Chute um número entre 1 e 1.000: "))
tentativas = 1
while chute < sorteado or chute > sorteado:
    if chute < sorteado :
        print("O número sorteado é MAIOR que o seu chute!")
    elif chute > sorteado :
        print("O número sorteado é MENOR que o seu chute!")
    else:
        print("O número sorteado é IGUAL ao seu chute!")
    print()
    chute = int(input("Chute outro número entre 1 e 1.000: "))
    tentativas +=1
print("Você acertou usando apenas {} chutes".format(tentativas))
