#IAM JUST GOING TO CREATE THE FUNCTION FOR CREATING SIMPLE CALCULATE :
#CALCULATE FUNCTION :
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

#OPEAROTS :
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# GETTING VALUE FROM USER :
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# FINAL CONDITION :
if operation in operations:
    result = operations[operation](num1, num2)
    print(f"Result: {result}")
else:
    print("Invalid operation")
