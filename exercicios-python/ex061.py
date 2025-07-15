'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando
a estrutura while
'''

primeiro_termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
fim = primeiro_termo + (razao * 9)

print(primeiro_termo, end = " -> ")

while (primeiro_termo < fim):
    primeiro_termo += razao
    print(primeiro_termo, end = " -> ")

print('ACABOU')