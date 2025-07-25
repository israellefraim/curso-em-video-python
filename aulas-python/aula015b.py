nome = "ISRAEL EFRAIM"
idade = "16"
valor = 3.14159

print(f"{nome:18} tem {idade} anos.")  # O nome tem 14 caracteres, então ele adiciona 4 espaços à direita para completar os 20.
print(f"{nome:^25} tem {idade} anos.")  # Centralizado no espaço de 25 caracteres reservados
print(f"{nome:>25} tem {idade} anos.")  # Alinhado a direita
print(f"{nome:<25} tem {idade} anos.\n")  # Alinhado a esquerda

print(f"{nome:*<25}")   # 'Israel****' — completa com * à direita
print(f"{nome:->25}")   # '----Israel' — completa com - à esquerda
print(f"{nome:.^25}\n")   # '..Israel..' — centraliza com pontos

print(f"{valor:.2f}")   # 3.14 (2 casas decimais)
print(f"{valor:-^10.2f}")  # Largura 10, centralizado com listras, com 2 casas decimais

num = 1234567
print(f"\n{num:,}")       # Separador de milhar

p = 0.075
print(f"\n{p:.2%}")  # Porcentagem