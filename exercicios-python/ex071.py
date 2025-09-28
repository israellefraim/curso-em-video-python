'''
Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

valor_sacado = int(input("Insira um valor a ser sacado: R$"))
total_valor = valor_sacado
valor_cedula = [50, 20, 10, 1]
i = 0

while valor_sacado > 0:
    quantidade_cedulas = valor_sacado // valor_cedula[i]
    if quantidade_cedulas > 0:
        print(f"Total de {quantidade_cedulas} cédula(s) de R${valor_cedula[i]}")
        valor_sacado -= (quantidade_cedulas * valor_cedula[i])
    i += 1
