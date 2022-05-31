num = int(input("Digite um número para saber se é primo ou não: "))

i = 1
soma = 0
while i <= num:
    if num % i == 0:
        soma+=1
    i+=1
if soma == 2 :
    print("É primo")
else:
    print("Não é primo")
    