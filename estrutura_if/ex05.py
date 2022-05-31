dias_uteis = int(input("Quantos dias úteis teve no mês? "))
horas_trabalho = float(input("Quantas horas foram trabalhadas pelo trabalhador? "))
sala_hora = float(input("Quantos reais você ganha por hora? "))
hora_total = dias_uteis * 8
salario =sala_hora * hora_total
# print(salario)
if horas_trabalho > hora_total:
    
    salario_extra = (horas_trabalho - hora_total) * sala_hora / 2
    salario = round (salario_extra + salario,2)
    print(salario)
else:
    salario = round (sala_hora * hora_total,2)
    print(salario)
    