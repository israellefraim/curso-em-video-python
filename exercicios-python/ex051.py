''' 
Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão.
'''

n1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
fim = n1 + (r * 10)
for c in range(n1, fim, r):
    print(f'{c}', end=' -> ')
print('ACABOU')
