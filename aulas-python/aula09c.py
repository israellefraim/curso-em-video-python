frase = "Curso em Vídeo Python"
print(frase.replace('Python', 'Android'))  # Substituição de uma antiga palavra ou caractere por outro
print(frase.upper())  # Faz todas as letras ficarem maiúsculas
print(frase.lower())  # Faz todas as letras ficarem minúsculas
print(frase.capitalize())  # Apenas a primeira letra da variável fica maiúscula
print(frase.title())  # Todas as primeiras letras das palavras ficam maiúsculas
print(frase.upper().count('O'))  # Combinação de duas funções diferentes
print(frase.lower().find('vídeo'))  # Após deixar tudo em mínusculo, ele diz a posição da palavra
frase = frase.replace('Python', 'Android')  # Substituindo de maneira permanente um termo por outro
print(frase)
