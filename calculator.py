def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if x == 0 or y == 0:
        return None
    else:
        return x / y

num_1 = int(input("Enter your first number: "))
num_2 = int(input("Enter your second number: "))

print("Sum:", add(num_1, num_2))
print("Difference:", subtract(num_1, num_2))
print("Product:", multiply(num_1, num_2))
print("Quotient:", divide(num_1, num_2))