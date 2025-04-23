grade_1 = float(input('Enter your first-grade score: '))
grade_2 = float(input('Enter your second-grade score: '))
average = (grade_1 + grade_2) / 2

if average < 5:
    print('\033[1;91mFAILED\033[m')
elif average <= 6.9:
    print('\033[1;93mRECOVERY\033[m')
else:
    print('\033[1;94mPASSED\033[m')
