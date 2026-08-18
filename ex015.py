n = int(input('Digite um numero para calcular seu Fatorial: '))
c = n
f = 1

print(f'Calculando {n}! = ', end='')
while c > 0:
    if c < n:
        print(' x ', end='')
    print(f'{c}', end='')
    f *= c
    c -= 1
print(f' = {f}')