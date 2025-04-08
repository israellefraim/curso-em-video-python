lar = float(input('Indique a \033[1;97mlargura\033[m da parede em metros: '))
alt = float(input('Indique a \033[1;97maltura\033[m da parede em metros: '))
area = alt * lar
tint = area / 2
print(f'\nA área da parede é de \033[93m{area}m²\033[m, e será gasto \033[91m{tint}\033[m litros de tinta.')
