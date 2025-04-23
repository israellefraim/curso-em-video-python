import random

action = ['ROCK', 'PAPER', 'SCISSORS']
symbol_computer = random.choice(action)

question = str(input("Let's play Rock, Paper, Scissors? (Y/N): ")).upper()

if question == 'Y':
    symbol_user = str(input('Write your choice: \n\nYOU: ')).upper()
    if symbol_user not in action:
        print('\033[91mINVALID ACTION. TRY AGAIN.')
    else:
        print(f'ROBOT: \033[91m{symbol_computer.capitalize()}\033[m')
        if symbol_computer == 'ROCK' and symbol_user == 'SCISSORS':
            print('\n\033[1;4mI WON')
        elif symbol_computer == 'SCISSORS' and symbol_user == 'PAPER':
            print('\n\033[1;4mI WON')
        elif symbol_computer == 'PAPER' and symbol_user == 'ROCK':
            print('\n\033[1;4mI WON')
        elif symbol_computer == symbol_user:
            print('\n\033[1;4mDRAW')
        else:
            print('\n\033[1;4mYOU WON')
else:
    print('Ok, have a good day :)')