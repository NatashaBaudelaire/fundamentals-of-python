largest = 0
smallest = 0
for c in range(1, 11):
    num = int(input(f'Enter the {c}th number: '))
    if c == 1:
        largest = num
        smallest = num
    else:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
print(f'The largest number entered is {largest}.')
print(f'The smallest number entered is {smallest}.')
