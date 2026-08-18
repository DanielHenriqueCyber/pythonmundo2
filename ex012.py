print("-*-*-* Bem vindo a Umbrela Copyright *-*-*-")
print("Vamos realizar o seu cadastro:")
cadastro = ""

while cadastro != "M" and cadastro != "F":
    cadastro = str(input("Digite o seu sexo: [M/F]")).upper()
    if cadastro == "M":
        print("Cadastrado com sucesso!")
        break
    elif cadastro == "F":
        print("Cadastrado com sucesso!")
        break
    else:
        print("Opção invalida! Tente novamente.")