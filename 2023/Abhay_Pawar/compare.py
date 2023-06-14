'''a=int(input("Enter the num1:"))
b=int(input("Enter the num2:"))
if(a>b):
     print(a," is greater")
else:
     print(b,"is greater")

print()
for i in range(11,0,-1):
     print(i)
print()
i=0
while(i<=10):
     print(i)
     i+=1
arr=[i for i in range(1,11)]
print(arr)'''

'''def recursion_fact(n):
     if(n==1 or n==0):
          return 1
     else:
          m=n*recursion_fact(n-1)
          return m
     
n=int(input("Enter the number :"))
m=recursion_fact(n)
print(m)'''

arr=[i for i in range(1,6)]
print(arr)
print(arr[:2])
print(arr[2:])
print(arr[:2:])
print(arr[5:0:-2])

