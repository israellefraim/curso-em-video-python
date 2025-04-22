year = int(input("Insira um ano para verificar se ele é \033[1;3;93mbissexto\033[m: "))
 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"\n\033[1;94m{year}\033[m é um ano \033[1;3;93mbissexto\033[m.")
else:
    print(f"\n\033[1;91m{year}\033[m não é um ano \033[1;3;93mbissexto\033[m.")
