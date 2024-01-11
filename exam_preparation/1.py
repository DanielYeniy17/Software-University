numbers = list(map(int, input().split(' ')))
while True:
    command = input().split(' ')
    if command[0] == 'swap':
        first = int(command[1])
        second = int(command[2])
        numbers[first], numbers[second] = numbers[second], numbers[first]
    elif command[0] == 'multiply':
        first = int(command[1])
        second = int(command[2])
        num = numbers[first] * numbers[second]
        numbers[1] = num
    elif command[0] == 'decrease':
        numbers = numbers - 1
    elif command[0] == 'end':
        break

print(' '.join(map(str, numbers)))
