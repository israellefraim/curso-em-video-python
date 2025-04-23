soma_idades = 0
maior_idade = 0
nome_maior_idade = ''
mulheres_novas = 0

for c in range(0, 4):
    nome = str(input(f'Insira o nome da {c+1}ª pessoa: ')).strip().capitalize()
    idade = int(input(f'Insira a idade da {c+1}ª pessoa: '))
    sexo = str(input(f'Insira o sexo da {c+1}ª pessoa (M/F): ')).strip().upper()
    soma_idades += idade
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_maior_idade = nome
    if sexo == 'F' and idade < 20:
        mulheres_novas += 1

media = soma_idades / 4
print(f'\nA média de idade do grupo é {media:.1f}')
print(f'O homem mais velho se chama {nome_maior_idade} e tem {maior_idade} anos')
print(f'Das 4 mulheres, {mulheres_novas} mulheres tem menos de 20 anos')
