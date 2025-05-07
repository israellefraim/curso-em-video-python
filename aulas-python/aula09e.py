frase = "Curso em Vídeo, Python"
print(frase.split())  # Dividiu a string em substrings a partir do espaço em branco entre as palavras por padrão
print('-'.join(frase.split()))  # Colocou o caractere '-' entre as divisões de palavras
print(frase.split(','))  # Dividiu a string a partir da vírgula
print(frase.split(' ', 2))  # Indica o número máximo de divisões a serem feitas, tendo como base os espaços em branco
print(list(frase))  # Este código transformará a string em uma lista de caracteres, onde cada letra será um elemento separado

dividido = frase.split()
print(dividido[0])  # Mostra o item 0 da lista
print(dividido[2][3])  # Mostra o valor do índice 3 do item 2 da lista
