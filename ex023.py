import random

v = 0

print("=-" * 15)
print("  VAMOS JOGAR PAR OU ÍMPAR!  ")
print("=-" * 15)

while True:
    usuario = int(input("Escolha um número: "))
    computador = random.randint(1, 10)
    total = usuario + computador

    escolha = ""
    # O loop continua enquanto a escolha não for P ou I
    while escolha not in ["P", "I"]:
        entrada = str(input("Ímpar ou Par? [P/I]: ")).strip().upper()
        if entrada:  # Garante que o usuário digitou alguma coisa antes de pegar a primeira letra
            escolha = entrada[0]

    print("-" * 35)
    print(f"Você jogou {usuario} e o computador {computador}. Total de {total}!")
    print("-" * 35)

    if total % 2 == 0:
        print("Deu PAR!")
        resultado = "P"
    else:
        print("Deu ÍMPAR!")
        resultado = "I"

    if escolha == resultado:
        print("Você VENCEU!")
        print("Vamos jogar novamente...")
        print("=-" * 15)
        v = v + 1
    else:
        print("Você PERDEU!")
        print("=-" * 15)
        break

print(f"GAME OVER! Você venceu {v} vezes.")