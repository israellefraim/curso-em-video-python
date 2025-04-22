from unidecode import unidecode

frase = str(input("Digite uma frase: ")).strip().upper() 
frase2 = unidecode(frase)

print(f"A letra \033[93mA\033[m aparece \033[97m{frase2.count('A')}\033[m vezes na frase.")
print(f"A primeira letra \033[93mA\033[m apareceu na posição \033[4;97m{frase2.find('A')+1}\033[m.")
print(f"A última letra \033[93mA\033[m apareceu na posição \033[4;97m{frase2.rfind('A')+1}\033[m.")  # Procurou o A da direita para esquerda
