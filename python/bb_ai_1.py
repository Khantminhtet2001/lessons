#simple calculator


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("The divisor cannot be zero")
    return x / y

def calculate(operation, x, y):
    if operation == "add":
        return add(x, y)
    elif operation == "subtract":
        return subtract(x, y)
    elif operation == "multiply":
        return multiply(x, y)
    elif operation == "divide":
        return divide(x, y)
    else:
        raise ValueError("Invalid operation")

while True:
    operation = input("Enter the operation (+, -, *, /): ")
    if operation.lower() == "exit":
        break

    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))

        result = calculate(operation, x, y)
        print(f"The result of {operation} {x} and {y} is {result}")
    except ValueError as ve:
        print(ve)