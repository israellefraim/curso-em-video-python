frase = str(input('Insira uma frase: ')).strip().lower().replace(' ', '')
print('A frase acima é um palíndromo' if frase == frase[::-1] else 'A frase acima não é um palíndromo')
