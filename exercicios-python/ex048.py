acum = 0
quant = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        acum += c
        quant += 1
print(f'A soma dos {quant} número é igual a {acum}')
