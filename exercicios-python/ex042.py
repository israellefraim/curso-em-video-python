from time import sleep as intervalo

a = float(input("Enter the length of the 1st side: "))
b = float(input("Enter the length of the 2nd side: "))
c = float(input("Enter the length of the 3rd side: "))

print("\n\033[1;7mPROCESSING...\033[m\n")
intervalo(3)

if a + b > c and a + c > b and b + c > a:
    
    if a == b == c:
        print("\033[94mThe sides entered form an equilateral triangle.\033[m")
    elif a == b or a == c or b == c:
        print("\033[94mThe sides entered form an isosceles triangle.\033[m")
    elif a != b != c != a:
        print("\033[94mThe sides entered form an scalene triangle.\033[m")

else:
    print("\033[91mAs retas inseridas não podem formar um triângulo.\033[m")
