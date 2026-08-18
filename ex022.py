cont = -1
while True:
    print("-="*30)
    tabuada = int(input("Quer ver a tabuada de qual numero? "))
    print("-="*30)
    cont = 0
    while True:
        cont = cont + 1
        resultado = tabuada * cont
        print(f" -->  {tabuada} x {cont} = {resultado} <--")
        if cont == 10:
            break
        
