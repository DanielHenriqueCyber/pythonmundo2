#Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a
# media atingida:
#Media abaixo de 5.0: Reprovado
#Media entre 5.0 e 6.9: Recuperação
#Media 7.0 ou superior: Aprovado

portugues = float(input("Digite sua nota em Portugues:"))
matematica = float(input("Digite sua nota em Matematica:"))
historia = float(input("Digite sua nota em Historia:"))
ciencias = float(input("Digite sua nota em ciencias:"))

notas = [portugues, matematica, historia, ciencias]
media = sum(notas) / 4

if media < 5.0:
    print(f"Sua nota foi {media}. Você esta reprovado.")
elif media >= 5.0 and media <= 6.9:
    print(f"Sua nota foi {media}. Você esta de recuperação")
else:
    print(f"Sua nota foi {media}. Voce esta aprovado")