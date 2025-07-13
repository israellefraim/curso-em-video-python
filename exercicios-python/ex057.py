sexo = "w"

while sexo not in ['M', 'F']:  # Se o texto digitado não for M nem F...
    sexo = str(input('Insira seu sexo (M/F): ')).strip().upper()[0]  # Pega somente a primeira letra da resposta
print(f'Sexo {sexo} registrado com sucesso!')