weight = float(input('Enter your weight (kg): '))
height = float(input('Enter your height (m): '))

IMC = weight/pow(height, 2)
print(f'\nIMC = {IMC:.1f}', end=' ')

if IMC < 18.5:
    print('\033[1;96mUNDERWEIGHT\033[m')
elif IMC < 25:
    print('\033[1;92mIDEAL WEIGHT\033[m')
elif IMC < 30:
    print('\033[1;93mOVERWEIGHT\033[m')
elif IMC < 40:
    print('\033[1;31mOBESITY\033[m')
else:
    print('\033[1;91mMORBID OBESITY\033[m')