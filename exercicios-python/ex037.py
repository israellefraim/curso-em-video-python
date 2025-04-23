num = int(input('Insira um número decimal inteiro: '))
print('''------------------
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
------------------''')
tipo_num = int(input('Escolha uma base de conversão: '))

if tipo_num == 1:
    print(f'({num})₁₀ = ({bin(num)[2:]})₂')
elif tipo_num == 2:
    print(f'({num})₁₀ = ({oct(num)[2:]})₈')
elif tipo_num == 3:
    print(f'({num})₁₀ = ({hex(num)[2:].upper()})₁₆')
else:
    print('\033[31mOpção inválida. Tente novamente.\033[m')
