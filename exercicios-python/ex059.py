from time import sleep

operacao = 0
valor1 = float(input("Insira o 1º valor: "))
valor2 = float(input("Insira o 2º valor: "))

while operacao != 5:
    print("\033[1;96m---------------------\033[m")
    print('''[1] SOMAR 
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    print("\033[1;96m---------------------\033[m")
    
    operacao = int(input("Escolha uma operação para realizar: "))
    
    if operacao == 1:
        soma = valor1 + valor2 
        print(f"\nSoma: {soma}\n")
    elif operacao == 2:
        multiplicacao = valor1 * valor2
        print(f"\nMultiplicação: {multiplicacao}\n")
    elif operacao == 3:
        maior_numero = max(valor1, valor2)
        print(f"\nMaior número: {maior_numero}\n")
    elif operacao == 4:
        valor1 = float(input("\nInsira o 1º valor: "))
        valor2 = float(input("Insira o 2º valor: "))

        print("\n\033[94mRECEBENDO NOVOS VALORES", end="", flush=True)
        sleep(1)
        print(".", end="", flush=True)
        sleep(1)
        print(".", end="", flush=True)
        sleep(1)
        print(".\n\033[m", flush=True)
        sleep(1)
    elif operacao == 5:
        print("\n\033[91m-PROGRAMA ENCERRADO-\033[m")
    else:
        print("\033[93mOpção inválida. Tente novamente.\033[m")
