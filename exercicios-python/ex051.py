''' 
Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão.
'''

primeiro_termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razao da PA: '))
fim = primeiro_termo + (razao * 10)
for c in range(primeiro_termo, fim, razao):
    print(f'{c}', end=' -> ')
print('ACABOU')
