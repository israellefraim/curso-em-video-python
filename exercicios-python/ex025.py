name = str(input("Digite seu \033[96mnome completo:\033[m ")).strip().upper().split()
print(f"Seu nome tem Silva? \033[95m{"SILVA" in name}\033[m")
