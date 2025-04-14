from random import choice
primeiro = str(input("Primeiro aluno: "))
segundo = str(input("Segundo aluno: "))
terceiro = str(input("Terceiro aluno: "))
quarto = str(input("Quarto aluno: "))
lista = [primeiro, segundo, terceiro, quarto]
result = choice(lista)
print(f"O aluno escolhido foi: \033[1;93m{result}")
