'''
Melhore o exercício 61, perguntando para o usuário
se ele quer mostrar mais alguns termos
O programa encerra quando ele disser que quer mostrar "0 termos"
'''

primeiro_termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))

contador = 0
limitador = 10
quantidade_termos = 0

while (contador < limitador):
    print(primeiro_termo, end = ' -> ')
    primeiro_termo += razao
    contador += 1
    quantidade_termos += 1
    if contador == limitador:
        print('PAUSA')
        limitador = int(input('\nQuantos termos você quer mostrar a mais? '))
        contador = 0

print(f'\nACABOU. Progressão finalizada com {quantidade_termos} termos mostrados.')
