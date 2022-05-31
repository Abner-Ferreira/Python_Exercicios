frase = str(input("Digite uma frase: "))
letras = (str(input("Digite um conjunto de letras: ")))
frase = frase.lower()
letras = letras.lower()
i = 0
y = 0
while i < len(letras): 
    frase = frase.replace(letras[y], "*")
    y+=1
    i+=1
print(frase)
    