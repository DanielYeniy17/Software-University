deck = list(map(str, input().split(':')))
result = []

while True:
    command = list(map(str, input().split(' ')))
    if command[0] == 'Ready':
        break

    if command[0] == 'Add':
        card = command[1]
        if card in deck:
            result.append(card)
        else:
            print('Card not found.')
    elif command[0] == 'Insert':
        card = command[1]
        index = int(command[2])
        if card in deck and 0 <= index < len(result):
            result.insert(index, card)
        else:
            print('Error!')
    elif command[0] == 'Remove':
        if command[1] in result:
            result.remove(command[1])
        else:
            print('Card not found.')
    elif command[0] == 'Swap':
        card1 = result.index((command[1]))
        card2 = result.index((command[2]))
        result[card1], result[card2] = result[card2], result[card1]
    elif command[0] == 'Shuffle' and command[1] == 'deck':
        result.reverse()

print(' '.join(map(str, result)))
