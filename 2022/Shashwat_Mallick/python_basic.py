def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1) 

number = 1
factorial(number)
print("The factorial of ",number," is ",factorial(number))
