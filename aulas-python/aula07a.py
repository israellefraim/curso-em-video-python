n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
print("A soma é {}, a subtração {}, o produto {}, a divisão {:.3}, a parte inteira da divisão {}, o resto da divisão "
      "{} e a exponenciação {}.".format(s, sub, m, d, di, r, e))
