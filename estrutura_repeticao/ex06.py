j = 1
i = 1
nota_maior = 0
nota_baixa = 70
alunoB = 0
alunoM = 0
alunoA = 0
while i <= 20 :
    nota_nova = int(input("{}° aluno, digite a sua nota: ".format(i)))
    
    if nota_nova >= 0 and nota_nova <= 20:
        alunoB +=1
        if nota_nova < nota_baixa:
            nota_baixa = nota_nova
        elif nota_nova > nota_maior:
            nota_maior = nota_nova

    elif nota_nova >= 21 and nota_nova <= 50:
        alunoM +=1
        if nota_nova < nota_baixa:
            nota_baixa = nota_nova
        elif nota_nova > nota_maior:
            nota_maior = nota_nova
       
    elif nota_nova > 50 and nota_nova <= 70:
        alunoA += 1
        if nota_nova < nota_baixa :
            nota_baixa = nota_nova
        elif nota_nova > nota_maior:
            nota_maior = nota_nova
    i+=1

print("- A MAIOR nota é {} .".format(nota_maior))
print("- A MENOR nota é {} .".format(nota_baixa))
print("- Porcentagem dos alunos que acertaram até 20 questões: {}% ".format((alunoB * 100) / 20))
print("- Porcentagem dos alunos que acertaram mais 21 questões e menos de 50 questões: {}% ".format((alunoM * 100) / 20))
print("- Porcentagem dos alunos que acertaram mais de 50 questões: {}% ".format((alunoA * 100) / 20))