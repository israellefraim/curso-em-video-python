num = int(input('Digite um número: '))
for c in range(1, 11):
    novo_num = num * c
    print(f'{num} x \033[1m{c}\033[m = {novo_num}')
