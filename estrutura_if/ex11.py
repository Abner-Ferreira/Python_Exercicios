from pprint import pprint


preco = float(input("Digite o valor do preço mostrado na etiqueta: "))
print("Qual seria a forma de pagamento? ")
print("-------------------------------------------")
print("(1) - A vista em dinheiro ou cheque")
print("(2) - A vista no cartão de crédito")
print("(3) - Em duas vezes")
print("(4) - Em quatro vezes")
print("-------------------------------------------")
codigo  = int(input("Digite o valor referente a forma de pagamento: "))
if codigo == 1 : 
    desconto = (preco * 10) / 100
    preco_novo= preco - desconto
    print("Com a forma de pagamento (1) o produto de {} reais passará a ser {} reais com desconto de 10%".format(preco, preco_novo))
elif codigo == 2 :
    desconto = (preco * 5) / 100
    preco_novo = preco - desconto 
    print("Com a forma de pagamento (2) o produto de {} reais passará a ser {} reais com desconto de 5%".format(preco, preco_novo))
elif codigo == 3 :
    print("Com a forma de pagamento (3) o valor do produto não tem alteração, ou seja, o preço será o mesmo")
elif codigo == 4 : 
    desconto = (preco * 7) / 100
    preco_novo = preco + desconto 
    print("Com a forma de pagamento (4) o produto de {} reais passará a ser {} reais com juros de 7%".format(preco, preco_novo))
else: 
    print("A forma de pagamento que você escolheu não tem na lista.")
