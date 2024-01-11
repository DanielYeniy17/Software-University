number =int(input())
positive = []
count_pos = 0
negative = []
sum_neg = 0
for i in range(number):
    numbers = int(input())
    if numbers >= 0:
        positive.append(numbers)
        count_pos += 1
    elif numbers < 0:
        negative.append(numbers)
        sum_neg += numbers
print(positive)
print(negative)
print(f'Count of positives: {count_pos}')
print(f'Sum of negatives: {sum_neg}')
