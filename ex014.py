primeiro = int
segundo = int
while True:
    primeiro = int(input("Primeiro numero:"))
    segundo = int(input("Segundo numero:"))
    opcao = str(input(" [1] Somar\n [2] Multiplicar\n [3] Maior\n >>>"))
    if opcao == "1":
        soma = primeiro + segundo
        print(f" A soma é {soma}")
    elif opcao == "2":
        multiplicar = primeiro * segundo
        print(f" A multiplicação é {multiplicar}")
    elif opcao == "3":
        if primeiro > segundo:
            print(f"O primeiro numero {primeiro} é maior que o segundo numero {segundo}")
        elif segundo > primeiro:
            print(f"O segundo numero {segundo} é maior que o primeiro numero {primeiro}")
        else:
            print(f"Os dois numeros são iguais")
    encontrou_opcao = False
    while not encontrou_opcao:
        print("E AGORA??")
        alternativa = str(input(" [4] Escolher novos numeros\n [5] Sair?"))
        if alternativa == "4":
            print("Reiniciando... Voltando ao menu principal!")
            encontrou_opcao = True
        elif alternativa == "5":
            print("Obrigado por utilizar o programa!")
            encontrou_opcao = True
            exit()