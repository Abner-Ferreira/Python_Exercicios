auxn = int(input("Digite um numero n:"))
n = auxn
i = n
aux = 1
permutacao = 1
while  i >= 1 :
    print(i)
    aux *= i
    auxn -= 1
    i -= 1 
print("O resultado da permutação de {} é {}".format(n,aux))    

