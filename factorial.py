def recular_factorial(n):
    if n == 1:
        return n
    else:
        return n*recular_factorial(n-1)

num = int(input("Enter a number "))

if num < 0:
    print("Sorry, factorials don't exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recular_factorial(num))