dia = int(input('Por quantos \033[1;97mdias\033[m esse carro foi alugado? '))
km = float(input('Quantos \033[1;97mkm\033[m foram rodados com este carro? '))
val1 = dia * 60
val2 = km * 0.15
val3 = val1 + val2
print(f'\nO valor total a pagar é de \033[92mR${val3:.2f}')
