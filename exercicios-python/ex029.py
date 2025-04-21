v = float(input("Insira a velocidade em que o carro está (\033[1;3mkm/h\033[m): "))

if v > 80:
    print(f"\nVocê \033[1;91mEXCEDEU\033[m o limite de velocidade de 80 km/h. A multa a ser paga é de \033[92mR${(v - 80) * 7 :.2f}\033[m")
else:
    print("\nVocê está \033[1;94mno limite\033[m de velocidade permitido.")
