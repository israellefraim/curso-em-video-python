gender = input('Are you a man (yes/no)? ').lower()
resposta = gender == 'yes'
if resposta:
    from datetime import date
    current = date.today().year
    year = int(input('Enter your year of birth: '))
    age = current - year

    if age < 18:
        saldo = 18 - age
        print(f'\nFaltam \033[1;34m{saldo}\033[m ano/s para você se alistar no serviço militar.')
        ano = current + saldo
        print(f'Seu alistamento será em {ano}')
    elif age == 18:
        print(f'\033[1;4;93mEstá na hora de se alistar para o serviço militar!\033[m')
    else:
        saldo = age - 18
        print(f'\033[1;4;91mO seu período de alistamento já passou {saldo} anos!\033[m')
        ano = current - saldo
        print(f'Seu alistamento foi em {ano}')
else:
    print("You don't need to enlist.")