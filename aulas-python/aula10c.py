n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
m = (n1 + n2) / 2
print(f"A sua média foi de {m:.1f}")
if m >= 6:
    print("Sua média foi boa!")
else:
    print("Sua média foi ruim!")

print("PARABÉNS" if m >= 6 else "ESTUDE MAIS!")
