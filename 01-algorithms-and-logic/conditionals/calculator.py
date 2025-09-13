def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero."
    return a / b

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
operation = input('1-addition\n2-subtraction\n3-multiplication\n4-division\nEnter the operation: ')

match operation:
    case '1':
        print(add(number1, number2))
    case '2':
        print(subtract(number1, number2))
    case '3':
        print(multiply(number1, number2))
    case '4':
        print(divide(number1, number2))
    case _:
        print('Invalid operation')
