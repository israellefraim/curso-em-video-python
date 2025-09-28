'''
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não a digitar os dados.
No final, mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1000.00
c) Qual é o nome do produto mais barato.
'''

nomes_produtos = []
valores_produtos = []
produto_mais_barato = ""
valor_total_produtos = produtos_caros = menor_valor = 0
i = 0

while True:
    nomes_produtos.append(str(input(f"\nNome do produto: ")))
    valores_produtos.append(float(input(f"Preço: R$")))
    valor_total_produtos += valores_produtos[i]
    if valores_produtos[i] > 1000:
        produtos_caros += 1
    if i == 0:
        menor_valor = valores_produtos[i]
        produto_mais_barato = nomes_produtos[i]
    elif valores_produtos[i] < menor_valor:
        menor_valor = valores_produtos
        produto_mais_barato = nomes_produtos[i]
    loop = str(input("Quer inserir outro produto? [S/N] ")).upper().strip()
    if loop == "N": 
        break
    i += 1

print(f"\nO total da compra foi R${valor_total_produtos}")
print(f"Temos {produtos_caros} produto(s) custando mais de R$1000,00")
print(f"O produto mais barato foi a/o {produto_mais_barato} que custa R${menor_valor:.2f}")
