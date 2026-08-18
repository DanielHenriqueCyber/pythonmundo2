total_imposto = 0
lista_compras = [100,250,150,200,350,400,300,450,600,1425,900]

for compras in lista_compras:
    # 1. Se a compra for maior que 1000, o imposto é 30% (compras * 0.30)
    if compras > 1000:
        imposto = compras * 0.30

    # 2. Se for maior ou igual a 500 (e menor que 1000), o imposto é 20%
    elif >= 500:
        imposto =0.20

    # 3. Para qualquer outro valor menor, o imposto é 10%
    else:
        imposto = 0.10

    # Seu acumulador (cofrinho) somando o imposto da rodada
    total_imposto = total_imposto + imposto
    pagamento_real = total_imposto + compras
# Como você daria um 'print' aqui no final para mostrar o 'total_imposto'?
print(f"O valor total da {pagamento_real} reais.")
