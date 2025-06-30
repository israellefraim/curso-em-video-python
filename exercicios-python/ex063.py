'''
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os primeiros n elementos e uma sequência de Fibonacci

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 (...)
'''

tamanho = int(input('Tamanho da sequência de finbonacci: '))
c1 = 1
c2 = 1
valor = 0
cont = 2
print(f'{c1} {c2} ', end="")

while (cont < tamanho):
    valor = c1 + c2
    print(valor, end=" ")
    c1 = c2
    c2 = valor
    cont += 1
    