


def primo (n1): 
    i = 1 
    soma = 0 
    while i <= n1 :
        if n1 % i == 0 :
            soma += 1
        i += 1
    if soma == 2 :
        resultado = "É primo"
    else : 
        resultado  = "Não é primo"
    return resultado

n1 = int(input("Digite o número que você quer saber se é primo ou não: "))
resp = primo(n1)
print(resp)