numA = float(input("Digite um número: "))
numB = float(input("Digite outro número: "))
op = input("Digite o operador que deseja usar (+ , - , * ou /): ")

soma = (op == "+")
subtracao = (op == "-")
multi = (op == "*")
divi = (op == "/")

if soma : 
    resultado = numA + numB
    print("{}".format (resultado))
elif subtracao : 
    resultado = numA - numB
    print("{}".format (resultado))
elif multi : 
    resultado = numA * numB
    print("{}".format (resultado))
elif divi : 
    if numB != 0 :
        resultado = numA / numB
        print("{}".format (resultado))
    else:
        print("Impossivel fazer divisao por 0, escolha outro numero")
else:
    print("------------ERRO------------")