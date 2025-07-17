''' 
Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos. O programa deve 
perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

resposta = 'S'
quantidade = soma = media = maior_numero = menor_numero = 0
lista = []

while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    lista.append(numero)
    resposta = str(input('Deseja continuar? [\033[32mS\033[m/\033[31mN\033[m] ')).strip().upper()[0]
    maior_numero = numero if numero > maior_numero else maior_numero 
    if quantidade == 1: menor_numero = maior_numero
    menor_numero = numero if numero < menor_numero else menor_numero 


media = soma/quantidade
print(f'\nVocê digitou {quantidade} número(s), e a média é {media:.2f}\nO maior número é {maior_numero} e o menor é {menor_numero}')
