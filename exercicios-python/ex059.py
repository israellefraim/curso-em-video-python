from time import sleep

while True:
    valor1 = float(input("Insira o 1º valor: "))
    valor2 = float(input("Insira o 2º valor: "))
    
    print("\033[1;96m---------------------\033[m")
    print("[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA")
    print("\033[1;96m---------------------\033[m")
    
    operacao = int(input("Escolha uma operação para realizar: "))
    
    if operacao == 1:
        soma = valor1 + valor2 
        print(f"Soma: {soma}")
        break
    elif operacao == 2:
        multiplicacao = valor1 * valor2
        print(f"Multiplicação: {multiplicacao}")
        break
    elif operacao == 3:
        maior_valor = max(valor1, valor2)
        print(f"Maior valor: {maior_valor}")
        break
    elif operacao == 4:
        print("\n\033[94mRECEBENDO NOVOS VALORES", end="", flush=True)
        sleep(1)
        print(".", end="", flush=True)
        sleep(1)
        print(".", end="", flush=True)
        sleep(1)
        print(".\n\033[m", flush=True)
        sleep(1)
    else:
        print("\n\033[91m-FINALIZANDO O PROGRAMA-\033[m")
        break
        