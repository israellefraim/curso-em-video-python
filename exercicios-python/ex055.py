maior_peso = 0
menor_peso = 0

for c in range(0, 5):
    peso = float(input(f'{c+1}) Insira seu peso em kg: '))
    if c == 0:
        maior_peso = peso
        menor_peso = peso
    else:
        if maior_peso < peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'O maior peso é: {maior_peso:.2f}kg\nO menor peso é: {menor_peso:.2f}kg')
