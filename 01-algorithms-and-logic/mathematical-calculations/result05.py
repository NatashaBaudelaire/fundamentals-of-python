num1 = int(input('Enter the first integer number: '))
num2 = int(input('Enter the second integer number: '))
sum_result = num1 + num2
if sum_result > 100:
    sum_result -= 10
    print(f'The sum is greater than 100. Subtracting 10, the final result is {sum_result}.')
else:
    print(f'The sum is {sum_result}.')
if sum_result == 100:
    print('The sum is exactly 100. Subtracting 10, the final result is 90.')
