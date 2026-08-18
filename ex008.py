lado1 = int(input("Digite a medida da primeira reta: "))
lado2 = int(input("Digite a medida da segunda reta: "))
lado3 = int(input("Digite a medida da terceira reta: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print("Seu triangulo é equilatero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Seu triangulo é Isósceles. ")
    else:
        print("Seu triangulo é Escaleno")
else:
    print("Essas medidas não pode formar um triangulo.")