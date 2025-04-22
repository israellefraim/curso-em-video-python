salario = float(input("\033[4mInsira o valor do seu salário:\033[m R$"))

if salario > 1250:
    print(f"\nParabéns! Você teve um aumento de 10%, portanto seu novo salário será de \033[1;92mR${salario * 1.10:.2f}\033[m")
else:
    print(f"\nParabéns! Você teve um aumento de 15%, portanto seu novo salário será de \033[1;92mR${salario * 1.15:.2f}")
