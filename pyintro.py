#If Else
'''
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
if a==b:
    print("Equal")
elif a>=b:
    print("Number 1 is greater")
else:
    print("Number 2 is greater")
'''

#For Loop
'''
for i in range(11,2,-1):
    print(i)

print(i)
'''

#While Loop
'''
i=0
while (i<=10):
    i+=1
    print(i)
'''

#Recursion
'''
num = int(input("Enter: "))
def fact(num):
    if (num==0) or (num==1):
        return(1)
    else:
        return num*fact(num-1)
print(fact(num))
'''

#List Slicing
'''
arr = [i for i in range (1,10)]
print(arr)
print(arr[:2])
print(arr[2:])
print(arr[2:5])
print(arr[0])
'''
