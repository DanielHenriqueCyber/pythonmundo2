#Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:

#O primeiro valor é maior
#O segundo valor é maior
# Nao existe valor maior, os dois são iguais

number1 = int(input("Digite um numero inteiro: "))
number2 = int(input("Digite outro numero inteiro: "))

if number1 > number2:
    print(f"O {number1} é maior que {number2}")
elif number2 > number1:
    print (f"O {number2} é maior que {number1}")
else:
    print(f"Os numeros {number1} e {number2} são iguais")