numbers = list(map(int, input().split(' ')))
average = sum(numbers) / len(numbers)
above_average = []
for i in range(len(numbers)):
    if numbers[i] > average:
        above_average.append(numbers[i])
        above_average.sort(reverse=True)

    else:
        pass

if len(above_average) == 0:
    print('No')
else:
    print(' '.join(map(str, above_average[:5])))
