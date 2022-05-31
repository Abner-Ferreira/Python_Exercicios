import math
def mediag (x , y): 
    raiz = x * y
    raiz = math.sqrt(raiz) 
    return raiz
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
resp = mediag(n1,n2)
print(resp)