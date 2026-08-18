#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
#tabela abaixo:

#Abaixo de 18.5: Abaixo do Peso
#Entre 18.5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade mórbida

nome = input("Qual o seu nome? ")
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

soma = peso / (altura * altura)

if soma < 18.5:
    print(f"Seu IMC é {soma}. {nome} está abaixo do peso.")
elif soma > 18.5 and soma <25:
    print(f"Seu IMC é {soma}. {nome} está com o peso ideal.")
elif soma > 25 and soma < 30:
    print(f"Seu IMC é {soma}. {nome} está com sobrepeso.")
else:
    print(f"Seu IMC é {soma}. {nome} está com obesidade morbida.")
