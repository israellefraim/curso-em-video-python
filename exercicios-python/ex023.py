num = int(input("Digite um \033[97mnúmero\033[m de 0 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Analisando o número \033[32m{num}\033[m...")
print(f"\033[96mUnidade: {u}") 
print(f"\033[92mDezena: {d}")
print(f"\033[94mCentena: {c}")
print(f"\033[95mMilhar: {m}")
