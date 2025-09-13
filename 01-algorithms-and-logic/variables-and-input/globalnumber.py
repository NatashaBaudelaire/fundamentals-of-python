number = 10

def function():
    global number
    number = 15
    return number

print(f'The initial value is {number}')
print(f'The value changed inside the function is {function()}')
print(f'The updated value now is {number}')