grausF = 50
while grausF <=150 :
    grausC = float(grausF - 32) / 1.8
    print("{}°F equivale a {:.2f}°Celsius".format(grausF,grausC))
    grausF+=1