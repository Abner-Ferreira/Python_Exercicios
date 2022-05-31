alunos = int(input("Digite o números de alunos na sala: "))
i = 0
soma = 0
acima = 0
abaixo = 0
while i != alunos : 
    nota = float(input("Digite a nota do aluno na primeira prova: ")) 
    soma += nota
    media = soma / alunos
    i+=1
    if nota >= 0 and nota < 5 :
        abaixo += 1
    elif nota > 5 and nota <= 10:
        acima += 1
    else :
        print("ERRO, nota inexistente.")
print("A média da sala é de {} , {} alunos tiraram menos que 5 e {} alunos tiraram mais que 5".format(media,abaixo,acima) )