idade = int(input("Digite a sua idade para saber a sua categoria: "))
if idade <= 4 : 
    print("Você tem {} anos e está na categoria bebê!".format(idade))
elif idade >= 5 and idade <= 7 :
    print("Você tem {} anos e está na categoria infantil!".format(idade))
elif idade >= 8 and idade <= 10 :
    print("Você tem {} anos e está na categoria juvenil!".format(idade))
elif idade >= 11 and idade <= 15 :
    print("Você tem {} anos e está na categoria adolescente!".format(idade))
elif idade >= 16 and idade <= 30 :
    print("Você tem {} anos e está na categoria adulto!".format(idade))
else  :
    print("Você tem {} anos e está na categoria senior!".format(idade))