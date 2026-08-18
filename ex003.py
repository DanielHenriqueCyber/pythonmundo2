#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar.
#Se já passou do tempo do alistamento.
#O programa deve tambem mostrar o tempo que falta ou que passou do prazo.

nome = str(input("Qual o seu nome: "))
ano_nascimento = int(input("Qual o ano de nascimento: "))
ano = 2026 - ano_nascimento
resultado2 = ano - 18
falta = 18 - ano

if ano == 18:
    print(f"Boa sorte, {nome}! Você está apto para realizar o alistamento")

elif ano >18:
    print(f"Seu alistamento está atrasado {resultado2} anos! Compareça a Junta Militar mais proxima urgentemente!")

elif ano <18:
    print(f"Ainda falta {falta} anos para o alistamento")

