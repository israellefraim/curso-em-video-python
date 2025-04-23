contador = 0
num = int(input('Insira um número: '))

for c in range(1, num+1):
    if num % c == 0:
        contador += 1
        print(f'\033[94m{c}\033[m', end=' ')
    else:
        print(f'\033[31m{c}\033[m', end=' ')

print(f'\nO número \033[32m{num}\033[m é um número', end=' ')
if contador == 2:
    print(f'\033[1mPRIMO\033[m, pois foi dividido {contador} vezes')
else:
    print(f'\033[1mCOMPOSTO\033[m, pois foi dividido {contador} vezes\033[m')