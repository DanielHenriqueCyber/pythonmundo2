num = 0
soma = 0
contador = -1
while True:
    soma = soma + num
    contador = contador + 1
    num = int(input("Digite um numero: [999 para parar] "))
    if num == 999:
        break
print(f" Foram {contador} digitos, e a soma de todos os numeros é {soma} ")