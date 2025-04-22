from time import sleep as intervalo
a = float(input("Insira o comprimento da 1ª reta: "))
b = float(input("Insira o comprimento da 2ª reta: "))
c = float(input("Insira o comprimento da 3ª reta: "))
print("\n\033[1;7mPROCESSANDO...\033[m\n")
intervalo(3)
if a + b > c and a + c > b and b + c > a:
    print("\033[94mAs retas inseridos podem formar um triângulo.")
else:
    print("\033[91mAs retas inseridas não podem formar um triângulo.")
