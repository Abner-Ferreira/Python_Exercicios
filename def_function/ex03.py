def primo (n1) : 
    i = 1 
    soma = 0 
    while i <= n1 :
        if n1 % i == 0 :
            soma += 1
        i+=1
    if soma == 2 :
        resp = True
    else :
         resp = False
    return resp
n1 = int(input("Digite um número para saber se é primo: "))
resultado = primo (n1)
print(resultado)
