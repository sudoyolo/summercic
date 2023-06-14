'''
a= int(input("Enter a number 1 :"))
b= int(input("Enter a number 2 :"))
if a==b :
    print("")
   
for i in range(11,2,-1):
    print(i)
 
print(i)

i= 0
while (i<=10):
    i+=1
    print(i)
    

arr =[i for i in range(1,11) ]

def factorial(n):
    if n==0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print("The factorial of given number is : ", result)
'''
arr =[i for i in range(1,11) ]
print(arr)
print(arr[::])
