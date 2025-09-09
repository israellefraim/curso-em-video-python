''' 
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo
'''

while True:
    numero = int(input('Digite o número de uma tabuada que deseja: '))
    if numero < 0: break
    for c in range(0, 11):
        if c == 0: 
            print(f"\033[1m{'TABUADA DO {numero}':^25}\033[m")
        print(f'{numero} x {c} = {numero * c}')
    print('\033[1m=-=-=-=-=-=-=-=-=--=\033[m')
    
print('\nPrograma encerrado.')