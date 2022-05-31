time1 = input("Digite o nome do primeiro time: ")
time2 = input ("Digite o nome do segundo time: ")
gol1 = int(input("Quantos gols o primeiro time fez? "))
gol2 = int(input("Quantos gols o segundo time fez? "))
if gol1 > gol2:
    print("O vencedor da partida foi", time1)
elif gol1 == gol2 : 
    print("A partida foi um empate")
else:
    print("O vencedor da partida foi", time2)