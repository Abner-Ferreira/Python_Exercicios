frase = str(input("Digite uma frase: "))
letra = str(input("Digite a letra que quer substituir na frase: "))

for aux in frase:
    if aux == letra.lower() or aux == letra.upper():
        aux = "*"
    print(aux)