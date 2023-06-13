a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a==b:
    print(a," and ", b ,"is equal")
elif a>=b:
    print(a," is greater than ",b)
else :
    print(b," is greater than ",a)
    

for i in range(11, 2, -1):
    print(i)
print(i) #output = 3 

i = 0
while(i<=11):
    i+=1
    print(i)

def factorial(n):
    if((n==0) or (n==1)):
        return 1
    else:
        return(n*factorial(n-1))
        

n = int(input("Enter n: "))
a = factorial(n)
print("factorial of ",n," is ",a)

arr = [i for i in range(1,10)]
print(arr)
print(arr[:2])
print(arr[2:])
print(arr[:2:])
print(arr[7:2])
print(arr[5:0:-1])
