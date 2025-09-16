sum_odds = 0
count = 0
for c in range(1, 101, 2):
    sum_odds += c
    count += 1
    print(c, end=' ')
    print(f'The sum of odd numbers between 1 and 100 is {sum_odds}.')
    print(f'The quantity of odd numbers between 1 and 100 is {count}.')