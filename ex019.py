n = 0
cont = 0
soma = 0
n = int(input("Digite um número [999 para parar]: "))
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input("Digite um número [999 para parar]: "))
print(f"A quantidade de numeros digitados foi {cont} e a soma foi {soma}")