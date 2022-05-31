n = int(input("Digite um número para ver se ele é perfeito ou não: "))
i = 1
soma = 0
ndiv = 0
while i < n :
    div = n % i
    if div == 0:
        soma += i
    else :
        ndiv +=i   
    i+=1
if n == soma :
    print("O número {} é perfeito ".format(soma))
else :
    print("O número {} não é perfeito".format(n))