nota1 = float(input('Digite sua primeira nota: \033[1;7;97m'))
nota2 = float(input('\033[mDigite sua segunda nota: \033[1;7;97m'))
media = (nota1 + nota2) / 2
print(f'\033[m\nA sua média é de \033[1;93m{media:.2f}\033[m')
