score = list(map(int, input().split('|')))
points = 0
while True:
    command = input().split('@')
    if command[0] == 'Game over':
        break

    if command[0] == 'Shoot Left':
        start = int(command[1])
        length = int(command[2])
        if
        score[start - length] -= 5
        points += 5
    elif command[0] == 'Shoot Right':
        start = int(command[1])
        length = int(command[2])
        n = int((start + length) / len(score))
        index = 0
        for i in range(n):
            if start + length > len(score):
                index = (start + length) - len(score)
        if index <= len(score):
            if 5 > score[index]:
                points += score[index]
            else:
                score[index] -= 5
                points += 5
    elif command[0] == 'Reverse':
        score.reverse()

print(' - '.join(map(str, score)))
print(f"John finished the archery tournament with {points} points!")

