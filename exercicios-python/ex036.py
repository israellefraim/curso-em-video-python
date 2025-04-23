yellow = '\033[33m'
red = '\033[1;31m'
blue = '\033[1;34m'
close = '\033[m'

house = float(input('Enter the house value: R$'))
salary = float(input('Enter your salary amount: R$'))
time = int(input('Enter how many years will you pay for the house: '))

installment = house / (time * 12)
print(f'\n{yellow}Salary: R${salary}{close}  |  {yellow}Time: {time * 12} months{close}', end='') # Por padrão print adiciona uma quebra de linha \n no final de cada print, e *end* muda isso, fazendo o final mudar para o que estiver dentro das aspas 
print(f'  |  {yellow}Installment: {installment:.2f}{close}')

if installment > (salary * 0.3):
    print('Loan request \033[1;31mDENIED\033[m')
else:
    print('Loan request \033[1;34mAPPROVED\033[m')
