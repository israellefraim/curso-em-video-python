import random
import time

numero_computador = random.randint(0, 11)
resposta = -1
palpites = 0

while resposta != numero_computador:
    resposta = int(input('Descubra qual número estou pensando de 0 a 10: '))
    palpites += 1
    print('\033[1mPROCESSANDO...\033[m')
    time.sleep(2)
    if resposta == numero_computador:
        print(f'\033[94mResposta correta! Você acertou após {palpites} tentativa(s)!\033[m')
    else:
        print(f'\033[91mTente novamente. A resposta é maior do que {resposta}.\033[m' if resposta < numero_computador else f'\033[91mTente novamente. A resposta é menor do que {resposta}.\033[m')
