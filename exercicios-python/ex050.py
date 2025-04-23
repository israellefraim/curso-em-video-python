soma = 0
quant = 0
for c in range(1, 7):
    num = int(input(f'Insira o {c}º número: '))
    if num % 2 == 0:
        soma += num
        quant+= 1
print(f'\033[1mA soma dos números pares é {soma}\033[m' if quant > 0 else 'Nenhum número par foi digitado.')
