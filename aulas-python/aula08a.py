import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'\nA raiz de {num} é igual a {math.floor(raiz)}')  # floor() arredonda para o número inteiro abaixo
print(f'\nA raiz de {num} é igual a {math.ceil(raiz)}')  # ceil() arredonda para o número inteiro abaixo
