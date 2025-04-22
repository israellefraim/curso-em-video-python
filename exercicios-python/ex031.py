distance = float(input("Insira a \033[1;3;97mdistância da viagem\033[m (km): "))

if distance <= 200: 
    print(f"O preço da passagem será de \033[92mR${distance * 0.5:.2f}\033[m")
else:
    print(f"O preço da passagem será de \033[92mR${distance * 0.45:.2f}\033[m")
