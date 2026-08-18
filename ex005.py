#A Confederaçã Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
#categoria, de acordo com a idade:
# Ate 9 anos: Mirim
# Ate 14 anos: infantil
# Ate 19 anos: Junior
# Ate 20 anos: Sênior
# Acima de 20 anos: Master

nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))

if idade <= 9:
    print(f"Sua idade é {idade} anos e você esta na Mirim.")
elif idade >9 and idade <= 14:
    print(f"Sua idade é de {idade} e você esta na Infantil.")
elif idade >14 and idade <= 19:
    print(f"Sua idade é de {idade} e você esta na Junior.")
elif idade >19 and idade <= 20:
    print("Sua idade é de {idade} e você esta na Senior.")
else:
    print(f"Sua idade é de {idade} e você esta na Master.")