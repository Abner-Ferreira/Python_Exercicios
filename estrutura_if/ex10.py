import math


a = float(input("Digite o primeiro coeficiente: "))
b = float(input("Digite o segundo coeficiente: "))
c = float(input("Digite o terceiro coeficiente: "))
delta = (b*b) -4*a*c


if a != 0 : 
    if delta >= 0 :
        x1 = (-b + (math.sqrt(delta))) / 2*a
        x2 = (-b - (math.sqrt(delta))) / 2*a
        print("{:.2f} e {:.2f} são os valores das raizes".format(x1,x2))

    else :
        print("Impossivel realizar a operação")
else : 
    print("Impossivel fazer a equação. O coeficiente (a) tem q ser diferente de 0.")
