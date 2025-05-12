import random
import time

numero_aleatorio = random.randint(0, 10)
resposta = -1
contador = 0

while resposta != numero_aleatorio:
    resposta = int(input('Descubra qual número estou pensando de 1 a 10: '))
    contador += 1
    print('\033[1mPROCESSANDO...\033[m')
    time.sleep(2)
    print(f"\033[94mVocê acertou após {contador} tentativa(s)!\033[m" if resposta == numero_aleatorio else "\033[91mTente novamente\033[m")