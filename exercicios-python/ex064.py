"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a 
condição de parada.No final, mostre quantos números foram digitado 
e qual foi a soma entre eles (desconsiderando o flag).
"""

numero = somador = contador = 0

numero = int(input('Digite um número (999 para parar): '))

while (numero != 999):
    somador += numero
    contador += 1 
    numero = int(input('Digite um número (999 para parar): '))
        
print(f'\nVocê digitou {contador} números e a soma entre eles foi {somador}.')
