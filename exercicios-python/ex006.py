num = float(input('Digite um valor: \033[1;4;97m'))
dob = num * 2
tri = num * 3
raiz = num ** (1/2)
print(
    f'\033[m\n\033[1;7;97mO dobro de {num} é {dob}\033[m '
    f'\n\033[1;7;97mO triplo é {tri}\033[m '
    f'\n\033[1;7;97mA raiz quadrada é {raiz:.2f}\033[m')
