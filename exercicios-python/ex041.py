from datetime import date
atual = date.today().year

year = int(input("Insira sua data de nascimento: "))
age = atual - year

print(f'O atleta tem {age} anos')
if age <= 9:
    print('Categoria: \033[1;96mMIRIM\033[m')
elif age <= 14:
    print('Categoria: \033[1;95mINFANTIL\033[m')
elif age <= 19:
    print('Categoria: \033[1;94mJUNIOR\033[m')
elif age <= 25:
    print('Categoria: \033[1;92mSÊNIOR\033[m')
else:
    print('Categoria: \033[1;93mMASTER\033[m')
