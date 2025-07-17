"""
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os primeiros n elementos e uma sequência de Fibonacci

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 (...)
"""

quantidade_termos = int(input('Quantidade de elementos da sequência: '))

termo1 = 0
termo2 = 1
termo3 = 0
contador = 2

while (contador <= quantidade_termos):   
    print(f'{termo3} -> ' if termo3 > 0 else '0 -> 1 -> ', end='')
    termo3 = termo1 + termo2 
    termo1 = termo2
    termo2 = termo3
    contador += 1

print('FIM')
