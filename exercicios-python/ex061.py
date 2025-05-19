primeiro_termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
fim = primeiro_termo + (razao * 9)

print(primeiro_termo, end = " -> ")

while (primeiro_termo < fim):
    print(primeiro_termo + razao, end = " -> ")
    primeiro_termo = primeiro_termo + razao


print('ACABOU')