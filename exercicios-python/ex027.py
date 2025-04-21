name = str(input("Digite o seu \033[1;95mnome completo\033[m: ")).title().strip().split()
print("\n\033[7mMuito prazer em te conhecer!\033[m")
print(f"Seu primeiro nome é \033[32m{name[0]}\033[m")
print(f"Seu último nome é \033[32m{name[-1]}\033[m\033[m")  # Os índices negativos são usados para acessar elementos a partir do final da lista. O -1 se refere ao último elemento da lista, - 2 ao penúltimo, etc.
