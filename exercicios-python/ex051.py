n1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
fim = n1 + (r * 10)
for c in range(n1, fim, r):
    print(f'{c}', end=' ⮕ ')
print('ACABOU')
