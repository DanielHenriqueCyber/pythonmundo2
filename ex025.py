preco = 0
produto_mil = 0
menor_preco = 0
nome_barato = ""
contador = 0

print("=-" * 30)
print("Loja Super Baratão")
print("=-" * 30)

while True:
    produto = str(input("Qual o nome do produto: "))
    valor = float(input("Qual o valor do produto: R$ "))
    contador = contador + 1

    # Acumula o total da compra
    preco = preco + valor

    # 1. Verifica se o PRODUTO atual custa R$1000 ou mais
    if valor >= 1000:
        produto_mil = produto_mil + 1

    # 2. Lógica para descobrir o mais barato
    if contador == 1:  # Se for o primeiro produto, ele é o mais barato
        menor_preco = valor
        nome_barato = produto
    else:  # Dos próximos em diante, compara com o menor já guardado
        if valor < menor_preco:
            menor_preco = valor
            nome_barato = produto

    # Validação simples para continuar
    next = " "
    while next not in "SN":
        next = str(input("Quer continuar? [S/N] ")).upper().strip()[0]

    if next == "N":
        break

print("=-" * 30)
print(f"O total da compra foi R${preco:.2f}")
print(f"Temos {produto_mil} produtos custando R$1000.00 ou mais.")
print(f"O produto mais barato foi {nome_barato} que custou R${menor_preco:.2f}")