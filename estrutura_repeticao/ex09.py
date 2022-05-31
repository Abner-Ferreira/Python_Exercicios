d = float(input("Digite o dinheiro inicial: "))
j = float(input("Digite o juros mensal:"))
t = int(input("Digite o tempo em meses: "))
i=0
while i < t :
    valor= (d * j) * t
    i+= 1
print(valor)

