#Escreva um programa para aprovar o emprestismo bancario para a compra de uma casa. O programa vai perguntar o valor da
#casa, o salario do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo sera negado.

nome = str(input('Digite seu nome: '))
valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Qual o seu salario:"))
duracao = int(input("Em quantas parcelas você gostaria de financiar:"))

valor_mensal = valor_casa / duracao
print(f"O valor mensal da casa é : R${valor_mensal:.2f}")

limite  = salario * 0.30
print(f"Seu limite é de R${limite:.2f}")

if limite >= valor_mensal:
    print("Seu financiamento esta aprovado, entre em contato com a central imobiliaria para dar continuidade:")
elif limite < valor_mensal:
    print(f"Infelizmente seu financiamento não pode ser aprovado. O limite passa de 30% da sua renda.")
