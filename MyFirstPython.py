'''python code done today (13/06/23)'''
'''BASIC INPUT OUTPUT and IF ELSE
print("Hello USER")
a=int(input("Enter first number: "))
b=int(input("Enter secnd number: "))

if a==b:
   print("both no.s are euqal")

elif a>b:
    print("the first no. is greater")

else:
    print("The second number is greater")
    '''




'''FOR LOOP
print("printing some even numbers")
 
for i in range(0,21,2):
   print(i)
   '''





'''if we use () instead of [] then we get a tuple which is imotable'''

'''LIST CREATION
A=[i for i in range(1,11)]

print(A)
A.append(1001)
print("After appenind 1001 to A ")
print(A)
   
i=10
print("Printing numbers from 10 to 20 using while")
while i<21:
     print(i)
     i+=1
'''






'''FUNCTION
n=int(input("Enter number whose factorial is to be calculated: "))

def Factorial(N):
    if N==0:
       return 1
    else:
        return N*Factorial(N-1)
    
print("The factorial is")
print(Factorial(n))
'''







'''SLICING
A=[i for i in range(1,26)]
print(A[0])
print(A[2:10])
print(A[:5])
print(A[22:])
'''








'''CLASS
class car:
    #init is like a constructor
    def init(self, name,):
        self.name=name

c1=car()
c1.name=input("Enter name of the first car: ")
print("your first car is a "+c1.name)
'''



