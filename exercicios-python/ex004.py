a = input('Digite algo: \033[1;4;97m')
print(f'\033[m\nO tipo primitivo é: \033[95m{type(a)}\033[m')
print(f'É alfabético? \033[1;94m{a.isalpha()}\033[m' if a.isalpha() else f'É alfabético? \033[1;91m{a.isalpha()}\033[m')
print(f'É numérico? \033[1;94m{a.isnumeric()}\033[m' if a.isnumeric() else f'É numérico? \033[1;91m{a.isnumeric()}\033[m')
print(f'É alfabético e numérico? \033[1;94m{a.isalnum()}\033[m' if a.isalnum() else f'É alfabético e numérico? \033[1;91m{a.isalnum()}\033[m')
print(f'Está em maiúsculas? \033[1;94m{a.isupper()}\033[m' if a.isupper() else f'Está em maiúsculas? \033[1;91m{a.isupper()}\033[m')
print(f'Está em minúsculos? \033[1;94m{a.islower()}\033[m' if a.islower() else f'Está em minúsculos? \033[1;91m{a.islower()}\033[m')
print(f'Só tem espaço? \033[1;94m{a.isspace()}\033[m' if a.isspace() else f'Só tem espaço? \033[1;91m{a.isspace()}\033[m')
print(f'Está capitalizado? \033[1;94m{a.istitle()}\033[m' if a.istitle() else f'Está capitalizado? \033[1;91m{a.istitle()}\033[m')
print(f'É um decimal? \033[1;94m{a.isdecimal()}\033[m' if a.isdecimal() else f'É um decimal? \033[1;91m{a.isdecimal()}\033[m')
print(f'Tem algo digitado? \033[1;94m{a.isdigit()}\033[m' if a.isdigit() else f'Tem algo digitado? \033[1;91m{a.isdigit()}\033[m')
