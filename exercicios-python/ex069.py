''' 
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos
'''

pessoas_adultas = quantidade_homens = mulheres_novas = 0

print("-CADASTRO DE PESSOAS-")

while True:
    genero = str(input("\nInsira seu gênero (M/F): ")).strip().upper()
    idade = int(input("Insira sua idade: "))

    if genero not in ["M", "F"] or 0 > idade > 130:
        print("\033[91mInsira um gênero e uma idade válida\033[m")
        continue
    else:
        if idade > 18:
            pessoas_adultas += 1
        if genero == "M":
            quantidade_homens += 1
        if genero in "F" and idade < 20:
            mulheres_novas += 1
        
        resposta_loop = str(input("Cadastrar mais pessoas (S/N): ")).strip().upper()
        if resposta_loop in "N":
            break

print(f"\n{pessoas_adultas} adulto(s) cadastrado(s)\n{quantidade_homens} homem(ns) cadastrado(s)\n{mulheres_novas} mulher(es) abaixo de 20 anos cadastrada(s)")
    




