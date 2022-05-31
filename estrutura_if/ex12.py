m_1sem = float(input("Digite qual foi sua media no primeiro semestre: "))
m_2sem = float(input("Digite qual foi sua media no segundo semestre: "))
mediaf = (m_1sem * 0.4) + (m_2sem * 0.6)
n_aula = int(input("Digite o número de aula que foi ministradas: "))
aula_ass = int(input("Digite o número de aula que foi assistidas: "))
freq = (n_aula * aula_ass) / 100
if mediaf >= 6 and freq >= 70:
    print("Você foi aprovado com média final {} e com frequência de {}% !".format(mediaf, freq))

else:
    if mediaf >=5 and freq <70 :
        print("Você foi reprovado, sua média final foi {} porém sua frequência foi {}%".format(mediaf,freq))
        print("------MOTIVO DA REPROVAÇÃO------")
        print("- Frequência menor que 70%")
    else:
        print("Você foi reprovado, sua média final foi {} e sua frequência foi {}%".format(mediaf,freq))
        print("------MOTIVO DA REPROVAÇÃO------")
        print("- Média final menor que 5")