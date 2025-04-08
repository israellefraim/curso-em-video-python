from math import hypot
opo = float(input('Digite o valor do \033[1;97mcateto oposto\033[m: '))
adj = float(input('Digite o valor do \033[1;97mcateto adjacente:\033[m '))
hip = hypot(adj, opo)
print(f'\nO valor da \033[1;94mhipotenusa\033[m é \033[32m{hip:.4f}\033[m')
