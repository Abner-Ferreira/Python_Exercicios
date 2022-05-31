alunos = int(input("Digite o números de alunos na sala: "))
i = 0
soma = 0
while i != alunos : 
    nota = float(input("Digite a nota do aluno na primeira prova: ")) 
    soma += nota
    i+=1
media = soma / alunos
print("A média da sala é de {}".format(media) )

    