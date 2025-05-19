#import math

num = int(input('Insira um número: '))
#print(math.factorial(numero))

total = 1

while (num >= 1):
    total = total * num
    num = num - 1
    
print(total)
    