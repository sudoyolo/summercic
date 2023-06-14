'''i=0
while(i<=10):
    i+=1
    print(i)'''
#FActorial

def factorial(n):
    if n==0 or n==1 :
        return 1
    else:
      return n*factorial(n - 1)

print(factorial(67))
            

