num1 = int(input("Enter the first integer number: "))
num2 = int(input("Enter the second integer number: "))
sum_result = num1 + num2
if sum_result > 100:
    result = sum_result - 10
    print("The result is:", result)
else:
    print("The sum of the numbers is:", sum_result)
    result = sum_result
    print("The result is:", result)
    print()