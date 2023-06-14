#if-else
'''
a= int(input("Enter number 1: "))
b= int(input("Enter number 2: "))
if a==b:
    print("Equal")
elif a>=b:
    print("Number 1 is greater")
else:
    print("Number 2 is greater")
'''

#python runs line by line

#for loop
'''
for i in range(1,11,2):
    print(i)
'''

#while loop
'''
i=0
while (i<=10):
    i+=1
    print(i)
'''   

#function
'''
def factorial(n):
    if (n==0) or (num==1):
        return 1
    else:
        return n*factorial(n-1)
num = int(input("Enter number: "))
result = factorial(num)
print("The factorial of", num, "is", result)
'''

#slicing
#indexing starts from zero
'''
arr = [i for i in range(1,10)]
print(arr)
print(arr[:2])
print(arr[2:])
print(arr[2:5])
print(arr[0])
'''
