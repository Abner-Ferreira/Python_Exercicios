n = int(input("Digite a quantidade de termos que vc quer colocar na sequencia: "))

i = 0
neg = 0
pos = 0

while i != n :
    num = float(input("Digite o numero da sequencia: "))
    i+=1
    if num < 0 :
        neg += 1 
    elif num > 0 :
        pos +=1 
print("Na sequencia tem {} números positivos e {} números negativos".format(pos, neg))