import random

print("Sou seu computador...")
print("Acabei de pensar em um numero entre 0 e 10.")
print("Será que você consegue adivinhar qual numero é?")
numero = int
tentativas = 0

while numero == numero:
    numero = random.randint(0, 10)
    palpite = int(input("Qual o seu palpite?"))
    tentativas = tentativas + 1
    if numero == palpite:
        print(f"Seu palpite etá certo! Eu pensei no numero {numero} e seu palpite foi {palpite}")
        print(f"Você acertou com {tentativas} tentativas")
        break
    else:
        print(f"Seu palpite está incorreto! Eu pensei em {numero} e seu palpite foi {palpite}")