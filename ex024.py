cont_idade = 0
m = 0
f = 0

print("=-" * 25)
print("CADASTRE UMA PESSOA")
print("=-" * 25)

while True:
    idade = int(input("Idade: "))
    if idade > 18:
        cont_idade = cont_idade + 1

    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]

    if sexo == "M":
        m = m + 1
    elif sexo == "F":
        f = f + 1

    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]

    if continuar == "N":
        break

print("=-" * 25)
print(f"O total de pessoas com mais de 18 anos: {cont_idade}")
print(f"Total de homens (M) cadastrados: {m}")
print(f"Total de mulheres (F) cadastradas: {f}")