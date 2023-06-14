for i in range(1,11,1):
    print(i)

k=int(input("Enter a number: "))
m=int(input("Enter a number: "))
if k>m:
    print(k," is greater than ",m)
else:
    print(m," is greater than ",k)
      
    

def recursion_factorial(n):
    if n==1:
        return n
    else:
        return n*recursion_factorial(n-1)
n = int(input("Enter a number : "))
if n<0:
    print(" Can't calculate factorial!")
elif n==0:
    print("Factorial is 0 ")
else:
    print("The Factorial of ",n," is ",recursion_factorial(n))
        
