'''
Melhore o exercício 61, perguntando para o usuário
se ele quer mostrar mais alguns termos
O programa encerra quando ele disser que quer mostrar "0 termos"
'''

quantidade_termos = int(input("Insira a quantidade de termos na PA: "))
if quantidade_termos < 1:
    exit()
primeiro_termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
fim = primeiro_termo + (razao * (quantidade_termos-1))

print(primeiro_termo, end = " -> ")

while (primeiro_termo < fim):
    print(primeiro_termo + razao, end = " -> ")
    primeiro_termo = primeiro_termo + razao


print('ACABOU')