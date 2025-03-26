n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = round((n1 / n2), 3)
di = n1 // n2
r = n1 % n2
e = n1 ** n2
print(
    f'A soma é {s}, \na subtração {sub}, \no produto {m}, \na divisão {round(d, 3)}, \na parte inteira da divisão {di},'
    f' \no resto da divisão {r} \ne a exponenciação {e}.')
