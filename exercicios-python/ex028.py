from random import randint
from time import sleep 
random_number = int(randint(0, 5))
print("\033[1;96m=-\033[m" * 31)
print("Duvido você adivinhar em qual número estou pensando de 0 a 5.")
print("\033[1;96m=-\033[m" * 31)
resposta = int(input("\nResposta: "))
print("\033[94mPROCESSANDO...\033[m")
sleep(3)
print("\033[1;92mACERTOU!!!\033[m" if resposta == random_number else f"\033[1;91mERROU\033[m (o número era {random_number})")
