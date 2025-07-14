''' 
Faça um programa que leia um número qualquer e mostre
o seu fatorial.

Ex.: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''

#import math
#print(math.factorial(numero))

'''
for c in range(numero, 0, -1):
    total *= numero
    print(f'{numero} x ' if numero != 1 else f'{numero} = {total}', end='')
    numero -= 1
'''

total = 1
numero = int(input('Insira um número: '))

print(f'{numero}! = ', end='')
while (numero >= 1):
    total *= numero
    print(f'{numero} x ' if numero != 1 else f'{numero} = {total}', end='')
    numero -= 1
