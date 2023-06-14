
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
result = factorial(num)
print("The factorial of", num, "is", result)









'''
class car:
    def _init_(self,color,brand,year):
    '''