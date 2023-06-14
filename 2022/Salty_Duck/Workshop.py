'''
a=int(input("enter number 1: "))
b=int(input("Enter number 2: "))
if a==b:
    print("Equal")
elif a>b:
    print("Number 1 is greater.")
else:
    print("Number 2 is greater.")

'''

'''
for i in range(11,2,-1):
    print(i)
    
'''

'''
i=0
while(i<=10):
    i+=1
    print(i)
    
'''

'''
arr=[i for i in range(1,11)]
print (arr)

'''

'''
def factorial(x):
    if(x==1 or x==0):
        return 1
    return x*factorial(x-1)
    
print(factorial(5))

'''

'''
arr=[i for i in range(1,11)]
print(arr)
print (arr[:3])
print (arr[3:])
print(arr[2:6])

'''
'''
class car:
    def __init__(self,name,brand,color,year):
        self.name = name
        self.brand = brand
        self.color = color
        self.year = year
my_car = car("rampayari","BMW","Black",2002)
print(my_car.name)

'''
