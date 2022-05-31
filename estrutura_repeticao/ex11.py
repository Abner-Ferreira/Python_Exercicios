n = int(input("Digite qual termo você quer saber de Fibonacci: "))
i = 2
n1 = 1
n2 = 1
print(n1)
print(n2)
while i < n :
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3)
    i+=1
