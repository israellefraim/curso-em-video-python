''' 
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou, 
no final do jogo.
'''

from random import randint
from unidecode import unidecode
from time import sleep

valor_jogador = quantidade_vitorias = 0

print("Vamos jogar ímpar ou par!")

while True:
    print("=--=" * 7)
    escolha_jogador = unidecode(str(input("Escolha \033[1;91mÍMPAR\033[m ou \033[1;92mPAR\033[m: "))).upper().strip()

    if escolha_jogador not in ["IMPAR", "PAR"]:
        print("Escolha entre '\033[1;91mÍMPAR\033[m' ou '\033[1;92mPAR\033[m'!")
        continue  # Pula imediatamente para a próxima iteração do loop, no início
    print("\033[1;91mÍMPAR\033[m")
    sleep(1)
    print("OU")
    sleep(1)
    print("\033[1;92mPAR\033[m!")
    valor_jogador = int(input("Insira um número: "))
    valor_computador = randint(0, 10)
    print(f"Meu número: {valor_computador}")
    soma_valores = valor_jogador + valor_computador
    
    if (soma_valores % 2) == 0:
        resultado = "PAR"
        if escolha_jogador == resultado:
            print("Você venceu!")
            quantidade_vitorias += 1
        else:
            print("Você perdeu!")
            break
    else:
        resultado = "IMPAR"
        if escolha_jogador == resultado:
            print("Você venceu!")
            quantidade_vitorias += 1
        else:
            print("Você perdeu!")
            break
print(f"\nVocê conseguiu vencer {quantidade_vitorias} vez(es)!")
print('\nJogo encerrado')