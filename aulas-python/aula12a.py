#  Exemplo estrutura condicional aninhada
name = str(input('Qual é seu nome? ')).strip()

if name == 'Gustavo': # Se quiser pode fazer estrutura condicional apenas com o if
    print('Que nome bonito!')
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif name in 'Ana Claúdia Jéssica Julian':
    print('Belo nome feminino.')
else: # Não precisa do else se não quiser colocar
    print('Seu nome é bem normal.')

print(f'Tenha um bom dia, {name}!')
