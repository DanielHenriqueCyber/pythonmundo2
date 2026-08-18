import time

#for tempo in range(10, -1, -1):
#    print(f"Contagem regressiva {tempo}")
#    time.sleep(1)



#for pares in range(0, 50, 2):
#    print(f" Os numeros pares são: {pares}")


#acumulador = 0
#cont = 0
#for soma in range(1, 501, 2):
#    if soma %3 ==0:
#        cont = cont + 1
#        acumulador = acumulador + soma
#print(f"A soma de todos os {cont} valores solicitados é {acumulador}")


#soma_idade = 0
#for pessoas in range(0, 4):
#    nome = str(input("Digite seu nome: "))
#    idade = int(input("Digite sua idade: "))
#    sexo = str(input("Digite seu sexo: "))
#    soma_idade += idade
#    media = soma_idade / 4
#    print(media)


#tabuada
#numero = int(input("Digite o valor que você deseja ver a tabuada:"))
#for tabuada in range(1,11):
#    print(f"{numero} x {tabuada}: {numero*tabuada}")

#Cronometro

#import time

#for tempo in range(10, -1, -1):
#    print(f" Contagem regressiva {tempo} segundos")
#    time.sleep(1)


vendas_vendedores = [
    {"nome": "Raissa", "valor": 6200},
    {"nome": "Diego", "valor": 3500},
    {"nome": "Catarina", "valor": 5000},
    {"nome": "Bruno", "valor": 4800},
    {"nome": "Luiza", "valor": 8000}
]

for lista in vendas_vendedores:
    if lista["valor"] >=5000:
        print(f"{lista['nome']} vendeu {lista['valor']} e o bonus é {lista['valor'] * 0.10}")
    else:
        print(f" O vendedor {lista['nome']} não bateu a meta e vendeu apenas {lista['valor']}")
        


