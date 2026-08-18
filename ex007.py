#Elabore um programa que calcule o valor a ser pego por um produto, considerando o seu preço normal e condiçao de pagamento:
# A vista dinheiro/cheque: 10% de desconto
# A vista no cartao: 5% de desconto
# Em ate 2x no cartao: preco normal
# Em 3x ou mais no cartao: 20% de Juros

preco = float(input("Qual o valor das compras: R$? "))
print("""FORMAS DE PAGAMENTO:
[1] À vista dinheiro
[2] À vista cartao
[3] 2x no cartao
[4] 3x ou mais no cartao""")
opcao = int(input("Qual é a opção desejada?"))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f}")
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input("Quantas parcelas? "))
    parcela = total / totalparc
    print(f"Sua compra R$: {total:.2f} vai custar: R${total:.2f} com juros.")
    print(f"Sua compra de {preco} vai custar R${total:.2f} ")
else:
    total = preco
    print ("Opção invalida, tente novamente.")
