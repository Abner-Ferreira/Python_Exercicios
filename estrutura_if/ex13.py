dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes em numero de 1 a 12: "))

if  dia >=1 and dia <= 31 and mes >= 1 and mes <= 12 :
    if mes == 1 or mes == 3 or mes == 5 or mes ==7 or mes==8 or mes==10 or mes==12:
        print("{}/{}".format(dia,mes))
        print("Data válida")
    elif mes == 2 and dia <= 28 :
        print("{}/{}".format(dia,mes))
        print("Data válida")
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia <= 30:
        print("{}/{}".format(dia,mes))
        print("{}/{}".format(dia,mes))
    else:
        print("{}/{}".format(dia,mes))
        print("Data inválida")
else:
    print("{}/{}".format(dia,mes))
    print("Data inválida")

    



