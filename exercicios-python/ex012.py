pre = float(input('Digite o preço de um produto: R$'))
desc = pre * 0.95
print(f'O novo preço do produto com \033[93m5%\033[m de desconto será de \033[32mR${desc:.2f}\033[m')
