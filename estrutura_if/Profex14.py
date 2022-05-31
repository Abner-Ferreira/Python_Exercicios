dia = int(input("Dia:"))
mes = int(input("Mes:"))
ano = int(input("Ano:"))

bissexto = False
if ano % 4 == 0 and ano %100 != 0 or ano % 400 == 0 :
    bissexto = True

if dia < 0 or dia > 31 or mes <1 or mes > 12 :
    print("data invalida")
elif mes == 2:
    if dia < 28:
        print("data valida")
    elif dia== 29 and bissexto == True :
        print("data valida")
    else:
        print("data invalida")
elif dia == 31 and (mes ==4 or mes==6 or mes == 9 or mes == 11):
    print("data invalida")
else:
    print("data valida")