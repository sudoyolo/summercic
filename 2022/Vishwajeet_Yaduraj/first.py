a = 2
b = 5
c = a + b
print (c);
for i in range(1,11,1):
    print(i)

'''print(i)   // this is how we do comments '''


i = 0
while(i<=10):
    i+=1
    print(i)

'''This is comment
a = int(input("Enter no. for Factorial"))

j=1
i=1
while(i<=a):
    i*=j '''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number =  int(input("Enter the Number for Factorial: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")

    
    
