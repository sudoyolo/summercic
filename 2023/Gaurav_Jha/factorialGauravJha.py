i = int(input("Enter a number: "))
def factorial(i):
    if i == 1 or i == 0:
        return 1
    else:
        return i * factorial(i-1)
result = factorial(i)
print(result)
