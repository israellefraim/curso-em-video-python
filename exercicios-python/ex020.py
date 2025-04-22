from random import shuffle
primeiro = str(input("Primeiro aluno: "))
segundo = str(input("Segundo aluno: "))
terceiro = str(input("Terceiro aluno: "))
quarto = str(input("Quarto aluno: "))
lista = [primeiro, segundo, terceiro, quarto] 
shuffle(lista)
print(f'\033[7;97mA ordem das apresentações será respectivamente: {lista[0]}, {lista[1]}, {lista[2]} e {lista[3]}.\033[m')
