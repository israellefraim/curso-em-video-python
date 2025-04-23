num1 = int(input('Enter a number (int): '))
num2 = int(input('Enter other number (int)'))

if num1 > num2:
    print('\nThe first value is greater.')
elif num2 > num1:
    print('\nThe second value is greater.')
else:
    print("\nThere is no greater value, both are the same.")
