def ocorrencia (frase, palavra):
    contador = 0
    pos = frase.find(palavra,0)
    while pos != -1:
        contador +=1
        pos = frase.find(palavra, pos+1)

    return contador
    
texto = str(input("Digite a frase que você quer saber: "))
word = str(input("Digite a palavra que você quer ver quantas vezes aparecem: "))

resp = ocorrencia(texto,word)
print(resp)