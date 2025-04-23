acum = 0
for c in range(0, 7):
    ano = int(input('Insira seu ano de nascimento: '))
    if ano <= 2007:
        acum += 1
print(f'\n{acum} pessoas já atingiram a maioridade.\n{7 - acum} ainda são menores de idade.')