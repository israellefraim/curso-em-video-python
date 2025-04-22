from time import sleep
nome = str(input("Escreva seu \033[1mnome completo\033[m: ")).strip()  # strip para tirar os espaços em branco desnecessários do início e do final
print("\n\033[1;95mAnalisando seu nome...\033[m")
sleep(3)
print('=-' * 30) 
print(f"\033[97mSeu nome em letras maiúsculas é {nome.upper()}.")
print(f"Seu nome em letras minúsculas é {nome.lower()}.")
print(f"Seu nome tem {len(''.join(nome.split()))} letras.")  # Primeiro separa as palavras para deixá-las sem espaços, dps junta novamente com join, e conta
dividido = nome.split()  # Cria uma lista com as palavras separadas
print(f"O seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras.")  # Conta quantas letras tem no espaço 0 da lista (primeiro nome)
print(f"O seu primeiro nome tem {nome.find(" ")} letras.")
