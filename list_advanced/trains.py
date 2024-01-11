wagons = int(input())
train = [0] * wagons
command = input()
tokens = command.split(' ')
while command != 'End':
    key_word = tokens[0]
    if key_word == 'add':
        people = tokens[1]
        train[-1] += int(people)
    elif key_word == 'insert':
        index = int(tokens[1])
        people = int(tokens[2])
        train[index] += people
    elif key_word == 'leave':
        index = int(tokens[1])
        people = int(tokens[2])
        train[index] -= people

print(train)
