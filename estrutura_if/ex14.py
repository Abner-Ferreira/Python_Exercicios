ano = int(input("Digite o ano:"))
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes em numero de 1 a 12: "))

if  ((ano%400==0)):
    if dia >= 1 and dia <= 31 and mes >=1 and mes <= 12:
        if mes == 1 or mes == 3 or mes == 5 or mes ==7 or mes==8 or mes==10 or mes==12:
            print("{}/{}/{}".format(dia,mes,ano))
            print("Data válida")

        elif mes == 2 and dia <= 29 :
            print("{}/{}/{}".format(dia,mes,ano))
            print("Data válida")

        elif (mes == 4 or mes == 6 or mes == 9 or mes == 1) and dia <= 30:
            print("{}/{}/{}".format(dia,mes,ano))
            print("Data válida")

        else:
            print("Data inválida")

    else:
        print("Data inválida")

elif ((ano%4)==0) and ((ano%100)!=0):

    if dia >= 1 and dia <= 31 and mes >=1 and mes <= 12:
        if mes == 1 or mes == 3 or mes == 5 or mes ==7 or mes==8 or mes==10 or mes==12:
            print("{}/{}/{}".format(dia,mes,ano))
            print("Data válida")

        elif mes == 2 and dia <= 29 :
            print("{}/{}/{}".format(dia,mes,ano))
            print("Data válida")

        elif (mes == 4 or mes == 6 or mes == 9 or mes == 1) and dia <= 30:
            print("{}/{}/{}".format(dia,mes,ano))
            print("Data válida")

        else:
            print("Data inválida")

    else:
        print("Data inválida")

else:
    
    if  dia >=1 and dia <= 31 and mes >= 1 and mes <= 12 :
        if mes == 1 or mes == 3 or mes == 5 or mes ==7 or mes==8 or mes==10 or mes==12:
         print("{}/{}/{}".format(dia,mes,ano))
         print("Data válida")

        elif mes == 2 and dia <= 28 :
            print("{}/{}/{}".format(dia,mes,ano))
            print("Data válida")

        elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia <= 30:
            print("{}/{}/{}".format(dia,mes,ano))
            print("Data válida")
            
        else:
            print("Data inválida")
    else:
        print("Data inválida")
   
   
   
   
   
   
   
   
   
   