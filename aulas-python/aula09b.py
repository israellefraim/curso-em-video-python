frase = "Curso em Vídeo Python"
print(len(frase))  # Tamanho da variável
print(frase.count('o'))  # Conta quantos 'o' tem na variável
print(frase.count('o', 0, 14))  # Conta quantos 'o' tem de um índice a outro
print(frase.find('u'))  # Procura na variável, e indica o ínicio dela na cadeia
print(frase.find('android'))  # Quando não existe na variável, leva para o índice -1
print('Curso' in frase)  # Valida se tem certo termo na variável com True ou False
