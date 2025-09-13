def sum_positives(values):
    total = 0
    for value in values:
        if value > 0:
            total += value
    return total

def count_negatives(values):
    count = 0
    for value in values:
        if value < 0:
            count += 1
    return count

numbers = []
for i in range(5):
    numbers.append(int(input("Enter an integer: ")))

sum_positives_result = sum_positives(numbers)
count_negatives_result = count_negatives(numbers)
print("The sum of the positive numbers is:", sum_positives_result)
print("The quantity of negative numbers is:", count_negatives_result)

# Exercise 2
def calculate_square(number):
    return number ** 2

def print_result(result):
    print("The square of the number is:", result)

number = int(input("Enter any number: "))
square = calculate_square(number)
print_result(square)